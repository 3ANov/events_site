from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

from events.models import Event
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
