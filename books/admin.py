from django.contrib import admin
from .models import Book, Comment


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'price')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'book', 'datetime_created')