from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from events.models import Event, EventInstance, Place, Category


class PlaceSerializer(serializers.ModelSerializer):
    geom = PointField()

    class Meta:
        model = Place
        exclude = ['id']
        read_only_fields = ['id']


class EventInstanceSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(many=False)

    class Meta:
        model = EventInstance
        exclude = ['id', 'event']
        read_only_fields = ['id']


class EventSerializer(serializers.ModelSerializer):
    event_instances = EventInstanceSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_instances', 'category']
        read_only_fields = ['id']

    def create(self, validated_data):
        event_instances = validated_data.pop('event_instances')
        event = Event.objects.create(**validated_data)

        for event_instance in event_instances:
            place = Place.objects.create(**event_instance.pop('place'))
            EventInstance.objects.create(event=event, place=place, **event_instance)

        return event
