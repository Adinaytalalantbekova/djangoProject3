from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('heloo/', views.hello_world, name='hello'),
    path('books/<int:id>/', views.BookListView.as_view(), name='books'),
    path('books/<int:id>/update/', views.BookUpdateView.as_view(), name="book_update"),
    path('add-book/', views.BookCreateView.as_view(), name='add_book'),
    path('books/<int:id>/delete/', views.BookDeleteView.as_view(), name='books')
]
