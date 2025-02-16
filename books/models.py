from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', default='default_image.jpg')
    translator = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publish_date = models.DateField()
    genre = models.CharField(max_length=100)
    pages_number = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
