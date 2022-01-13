from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_world(request):
    return HttpResponse('Hello World')


def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def books_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, 'book_list.html',{'books': books})



