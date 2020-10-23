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
    pagination_class = StandardResultsSetPagination
    serializer_class = EventSerializer

    permission_classes = [AllowAny]

    def get(self, request):
        try:
            lat = float(request.query_params.get('lat', None))
            long = float(request.query_params.get('long', None))
            radius = float(request.query_params.get('radius', None))

            point = Point(long, lat)
            result_set_events = Event.objects.filter(event_instances__in=EventInstance.objects.filter(
                place__in=Place.objects.filter(
                    geom__distance_lt=(point, D(km=radius)))))

            serializer = self.serializer_class(result_set_events, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'Value error'})



