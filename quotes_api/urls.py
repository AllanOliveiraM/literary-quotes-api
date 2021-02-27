"""Quotes_api URL Configuration."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('core.urls')),
    path('admin/', admin.site.urls),
]
