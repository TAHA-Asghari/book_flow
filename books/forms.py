from django import forms
from .models import Book, Comment


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
