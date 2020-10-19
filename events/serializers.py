from rest_framework import serializers

from events.models import Event, EventInstance


class EventInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInstance
        exclude = ['event']


class EventSerializer(serializers.ModelSerializer):
    event_instances = EventInstanceSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'event_instances']
        read_only_fields = tuple('id')

