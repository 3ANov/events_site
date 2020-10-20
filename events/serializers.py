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
    category = serializers.CharField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_instances', 'category']
        read_only_fields = ['id']

    def create(self, validated_data):
        event_instances = validated_data.pop('event_instances')
        category = Category.objects.get_or_create(name=validated_data.pop('category'))[0]
        event = Event.objects.create(category=category, **validated_data)
        for event_instance in event_instances:
            place = Place.objects.create(**event_instance.pop('place'))
            EventInstance.objects.create(event=event, place=place, **event_instance)

        return event

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
