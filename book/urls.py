from django.urls import path
from . import views
urlpatterns = [
    path('heloo/', views.hello_world, name='hello'),
    path('books/', views.book_all, name='books')
]