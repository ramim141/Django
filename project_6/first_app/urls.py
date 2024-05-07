from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    
    path('', views.home, name='home'),
    path('delete/<int:roll>', views.student_delete, name='delete'),
]
