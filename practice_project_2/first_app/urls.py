
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Meal_Card, name="Meal_Card"),
]
