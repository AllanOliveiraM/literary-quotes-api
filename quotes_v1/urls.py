from django.urls import path

from quotes_v1.views import root

urlpatterns = [
    path('root/', root),
]
