from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    update_data =models.DateTimeField(auto_now=True)
