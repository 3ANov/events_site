from django.contrib import admin
from .models import Event, EventInstance, Place, Category

# Register your models here.
admin.site.register(Event)
admin.site.register(EventInstance)
admin.site.register(Place)
admin.site.register(Category)