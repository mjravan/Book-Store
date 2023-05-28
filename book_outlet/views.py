from django.shortcuts import render

from .models import Book

# Create your views here.

def index(requst):
    books = Book.objects.all()
    return render(requst, "book_outlet/index.html", {
        "books": books
    })