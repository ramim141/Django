from django.shortcuts import render, redirect
from . models import Category
from . forms import CategoryForm
from django.contrib import messages

# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request,'category_list.html',{'categories':categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('add_category')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


