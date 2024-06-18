from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musician
from .forms import MusicianForm

class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    context_object_name = 'musicians'

class MusicianCreateView(CreateView):
    model = Musician
    template_name = 'musician_form.html'
    form_class = MusicianForm
    success_url = reverse_lazy('musician_list')

class MusicianUpdateView(UpdateView):
    model = Musician
    template_name = 'musician_form.html'
    form_class = MusicianForm
    success_url = reverse_lazy('musician_list')

class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = 'musician_delete.html'
    success_url = reverse_lazy('musician_list')
