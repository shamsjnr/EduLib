from django.urls import path
from . import views

urlpatterns = [
  path('books/', views.books, name='books'),
  path('add-book/', views.add_book, name='addBook'),
  path('update-book/<int:book_id>/', views.update_book, name='updateBook'),
  path('delete-book/<int:book_id>/', views.delete_book, name='deleteBook'),
  path('', views.index, name='home')
]