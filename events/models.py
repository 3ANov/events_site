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
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EventInstance(models.Model):
    """Инстанс мероприятия"""
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
