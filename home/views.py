from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Library
from .forms import LibraryForm

def add_Book(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_Library')
    else:
        form = LibraryForm()
    return render(request, 'add_Book.html', {'form': form})

def display_Book(request):
    Library = Library.objects.all()
    return render(request, 'display_Book.html', {'Library': Book})

def edit_Book(request, id):
    Library = get_object_or_404(Library, id=id)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=Library)
        if form.is_valid():
            form.save()
            return redirect('display_Library')
    else:
        form = LibraryForm(instance=Library)
    return render(request, 'edit_Library.html', {'form': form, 'Library': Library})

def delete_Book(request, id):
    Library = get_object_or_404(Library, id=id)
    Library.delete()
    return redirect('display_Book')