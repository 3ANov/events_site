from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Event, EventInstance, Place, Category

# Register your models here.
admin.site.register(Event)
admin.site.register(EventInstance)
admin.site.register(Place, LeafletGeoAdmin)
admin.site.register(Category)