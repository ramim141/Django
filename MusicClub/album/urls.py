from django.urls import path
from . import views  # Import views from the local module

urlpatterns = [
    path('albums/', views.album_list, name='album_list'),  # Use views.album_list_view
    path('add/', views.add_album, name='add_album'),
    path('edit/<int:pk>/', views.edit_album, name='edit_album'),
    path('delete/<int:pk>/', views.delete_album, name='delete_album'),
]
