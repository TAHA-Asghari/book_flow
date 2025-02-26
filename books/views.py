from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import comment
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import NewBookForm,NewCommentForm
from .models import Book, Comment


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'books/books_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView, generic.CreateView):
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = 'book'
    form_class = NewCommentForm

class CommentCreateView(LoginRequiredMixin,generic.CreateView):

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = NewCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book #assign current Book
            comment.user = request.user  # Assign the logged-in user
            comment.save()

        return redirect('book_details', pk=book.pk)


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = NewBookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = NewBookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
