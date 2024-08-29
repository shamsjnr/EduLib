from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
  return render(request, "index.html")


# List books
def books(request):
  book_list = Book.objects.all()
  return render(request, "books.html", {"books": book_list})


# Add a book...
def add_book(request):
  if (request.method == 'POST'):
    form = BookForm(request.POST)
    if (form.is_valid()):
      form.save()
      messages.success(request, "'" + request.POST['title'] + "' added to books")
      return redirect('books')
  else:
    form = BookForm()
  return render(request, "add_book.html", {"form": form})


# Update book details...
def update_book(request, book_id):
  book = Book.objects.get(id=book_id)
  if (request.method == 'POST'):
    form = BookForm(request.POST, instance=book)
    form.save()
    messages.success(request, "Book details updated successfully")
    return redirect('books')
  else:
    form = BookForm(instance=book)
    
  return render(request, "update_book.html", {"form": form, "book_id":book.id})


# Remove a book
def delete_book(request, book_id):
  book = Book.objects.get(id=book_id)
  if (book.id):
    book.delete()
    messages.success(request, "'" + book.title + "' deleted successfully")
  
  return redirect("books")
