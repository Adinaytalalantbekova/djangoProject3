from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms


def hello_world(request):
    return HttpResponse('Hello World')


def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})


def books_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_update(request, id, redirect=None):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books: book_all"))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'book_update.html', {"form": form,'object': book_object})



def show_delete(request,id):
    show_object = get_object_or_404(models.Book, id=id)
    show_object.delete()
    return HttpResponse('Show Deleted')
