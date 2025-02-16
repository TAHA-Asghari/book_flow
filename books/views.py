from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import NewBookForm
from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    form_class = NewBookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = NewBookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(generic.edit.DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
