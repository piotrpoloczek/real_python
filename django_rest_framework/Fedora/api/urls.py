from django.urls import path, include
from rest_framework.routers import

from . import views


urlpatterns = [
    path("v1/listing/", views.listing),
]