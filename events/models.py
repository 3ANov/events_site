from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    x = models.DecimalField(max_digits=9, decimal_places=6)
    y = models.DecimalField(max_digits=8, decimal_places=6)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EventInstance(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
