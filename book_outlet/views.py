from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.

def index(requst):
    books = Book.objects.all()
    return render(requst, "book_outlet/index.html", {
        "books": books
    })
def book_detail(requset, id):
    #try:
    #    book = Book.objects.get(pk=id)
    #except:
    #    raise Http404()
    book = get_object_or_404(Book, pk=id)
    return render(requset, "book_outlet/bookdetail.html",{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })