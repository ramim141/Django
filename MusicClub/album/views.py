from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})

def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    album.delete()
    return redirect('album_list')