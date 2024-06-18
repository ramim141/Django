from django.urls import path
from .views import MusicianListView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView

urlpatterns = [
    path('musicians/', MusicianListView.as_view(), name='musician_list'),
    path('musicians/add/', MusicianCreateView.as_view(), name='add_musician'),
    path('musicians/edit/<int:pk>/', MusicianUpdateView.as_view(), name='edit_musician'),
    path('musicians/delete/<int:pk>/', MusicianDeleteView.as_view(), name='delete_musician'),
]
