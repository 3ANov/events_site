from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer


class EventsSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get', 'post', 'put']
