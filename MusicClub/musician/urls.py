from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('add/', views.add_musician, name='add_musician'),
    path('edit/<int:pk>/', views.edit_musician, name='edit_musician'),  # Correct view function for editing
    path('delete/<int:pk>/', views.delete_musician, name='delete_musician'),  # Correct view function for deleting
]
