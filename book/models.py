from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    release_date = models.DateTimeField(auto_now_add=True)
    update_data =models.DateTimeField(auto_now=True)

def __str__(self):
    return f'{self.name}'



class BookComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_comment")
    text = models.TextField()
    created_data = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.books.title
