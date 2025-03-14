from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.urls import reverse
from django.utils.timezone import now



class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=100, unique=True,  # Ensures no duplicate titles
                             error_messages={"unique": "A book with this title already exists."})
    author = models.CharField(max_length=100,
                              validators=[
                                  RegexValidator(r'^[a-zA-Z\s]+$', "Author name can only contain letters and spaces.")
                              ])
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', default='default_image.jpg')
    translator = models.CharField(max_length=100,blank=True,null=True, validators=[
        RegexValidator(r'^[a-zA-Z\s]+$', "Author name can only contain letters and spaces.")
    ])
    publisher = models.CharField(max_length=100)
    publish_date = models.DateField(
        validators=[MaxValueValidator(limit_value=now().date(), message="Publish date cannot be in the future.")])
    genre = models.CharField(max_length=100)
    pages_number = models.PositiveIntegerField(validators=[MinValueValidator(1, "Page number must be at least 1.")])
    price = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(0, "Price must be a positive number.")])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_details', args=[self.id] )


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='unique_user_book_comment')
        ]

    def __str__(self):
        return f'{self.user}: {self.text}'