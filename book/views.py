from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_world(request):
    return HttpResponse('Hello World')


def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})


