from django.urls import path
from .views import AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('albums/', AlbumListView.as_view(), name='album_list'),
    path('albums/add/', AlbumCreateView.as_view(), name='add_album'),  # Ensure this line is correct
    path('albums/<int:pk>/edit/', AlbumUpdateView.as_view(), name='edit_album'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name='delete_album'),
]
