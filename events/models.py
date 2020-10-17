from django.db import models

# Create your models here.


class EventInstanse(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField()


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    event_instanse = models.ForeignKey()
