from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = NewCommentForm()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     # self.object = self.get_object()
    #     form = NewCommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.book = self.object
    #         comment.user = request.user
    #         comment.save()
    #         return redirect('book_details', pk=self.object.pk)
    #     return self.get(request, *args, **kwargs)

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = NewBookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class BookDeleteView(LoginRequiredMixin,UserPassesTestMixin, generic.edit.DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user