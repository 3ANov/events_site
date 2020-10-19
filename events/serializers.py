from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from events.models import Event, EventInstance, Place


class PlaceSerializer(serializers.ModelSerializer):
    geom = PointField()

    class Meta:
        model = Place
        fields = '__all__'


class EventInstanceSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(many=False)

    class Meta:
        model = EventInstance
        exclude = ['event']


class EventSerializer(serializers.ModelSerializer):
    event_instances = EventInstanceSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'event_instances']
        read_only_fields = ['id']


