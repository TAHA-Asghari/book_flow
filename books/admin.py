from django.contrib import admin
from .models import Book

@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'price')