from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    event_instances = serializers.StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'event_instances']
        read_only_fields = tuple('id')

