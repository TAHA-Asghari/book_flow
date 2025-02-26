from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_details'),
    path('new_post/', views.BookCreateView.as_view(), name='book_add'),
    path('<int:pk>/modify/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='add_comment'),

]
