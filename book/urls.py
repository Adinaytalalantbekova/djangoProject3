from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('heloo/', views.hello_world, name='hello'),
    path('books/<int:id>/', views.book_all, name='books'),
    path('add-book/', views.add_book, name='add_book'),
    path('books/<int:id>/delete/', views.books_detail, name='books')
]
