from django.contrib import admin
from django.urls import path, include, re_path

from events_site.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', IndexTemplateView.as_view(), name="entry-point"),
]
