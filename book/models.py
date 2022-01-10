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
