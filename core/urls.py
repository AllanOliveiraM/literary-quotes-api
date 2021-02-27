from django.urls import path, include

urlpatterns = [
    path('v1/', include('quotes_v1.urls')),
]
