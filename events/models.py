from django.db import models
from django.contrib.gis.db import models as gismodels


class Category(models.Model):
    """ Категория мероприятия """
    """ пример: 'концерт', 'тур' """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    """Место провидения мероприятия"""
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    geom = gismodels.PointField()

    def __str__(self):
        return self.name


class Event(models.Model):
    """Мероприятие"""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EventInstance(models.Model):
    """Инстанс мероприятия"""
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_instances')

    def __str__(self):
        return '%d: Место: %s  Город: %s %s %s' % (self.id, self.place.name,  self.place.city, self.time_start, self.time_end)
