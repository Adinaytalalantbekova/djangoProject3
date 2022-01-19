from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.views import generic


def hello_world(request):
    return HttpResponse('Hello World')

class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.filter().order_by("-id")


# def book_all(request):
#     book = models.Book.objects.all()
#     return render(request, 'book_list.html', {'book': book})

class BookDetailView(generic.DetailView):
    template_name = "book_detial.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=shows_id)


# def books_detail(request, id):
#     books = get_object_or_404(models.Book, id=id)
#     return render(request, 'book_list.html', {'books': books})

class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)



# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book created')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_book.html', {'form': form})

class BookUpdateView(generic.UpdateView):
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=shows_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)



# def book_update(request, id, redirect=None):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books: book_all"))
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, 'book_update.html', {"form": form,'object': book_object})

class BookDeleteView(generic.DetailView):
    template_name = "confirm_delete_book.html"
    success_url = '/books/'

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=shows_id)

# def show_delete(request,id):
#     show_object = get_object_or_404(models.Book, id=id)
#     show_object.delete()
#     return HttpResponse('Show Deleted')
