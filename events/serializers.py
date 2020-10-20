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
    category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_instances', 'category']
        read_only_fields = ['id']

    def create(self, validated_data):
        event_instances = validated_data.pop('event_instances')
        category = validated_data.pop('category', None)

        event = Event.objects.create(category=Category.objects.get_or_create(**category)[0],
                                     **validated_data)
        for event_instance in event_instances:

            place_data = validated_data.pop('place', None)
            print(place_data)
            if place_data:
                place = Place.objects.get_or_create(**place_data)[0]
                validated_data['place'] = place
                EventInstance.objects.create(event=event, place=place, **event_instance)
            else:
                raise serializers.ValidationError(
                    'Not place data'
                )
        return event

