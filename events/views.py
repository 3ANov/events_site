from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event, Place, EventInstance
from events.serializers import EventSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'per_page'
    max_page_size = 10


class EventsSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get', 'post', 'put']
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    filterset_fields = ('category',)


class EventDistanceView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        paginator = StandardResultsSetPagination()

        lat = float(request.query_params.get('lat', None))
        long = float(request.query_params.get('long', None))
        radius = request.query_params.get('long', None)

        point = Point(long, lat)
        result_set_events = EventInstance.objects.filter(
            place__in=Place.objects.filter(
                geom__distance_lte=(point, D(km=radius))))\
            .values('event')
        print(result_set_events)
        result_page = paginator.paginate_queryset(result_set_events, request)
        serializer = EventSerializer(result_page, many=True, context={'request': request})
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response
