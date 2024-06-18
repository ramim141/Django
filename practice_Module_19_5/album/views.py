from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album
from .forms import AlbumForm

class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'albums'

class AlbumCreateView(CreateView):
    model = Album
    template_name = 'album_form.html'
    form_class = AlbumForm
    success_url = reverse_lazy('add_album')  


class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'album_form.html'
    form_class = AlbumForm
    success_url = reverse_lazy('album_list')

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_delete.html'
    success_url = reverse_lazy('album_list')
