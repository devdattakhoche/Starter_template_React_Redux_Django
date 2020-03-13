from django.urls import path
from .views import start
urlpatterns = [
    path('starter_template/',start),
]