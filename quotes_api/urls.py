"""Quotes_api URL Configuration."""

from django.contrib import admin
from django.urls import path, re_path, include

from core.responses import bad_request

urlpatterns = [
    path('api/', include('core.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^.', bad_request)
]
