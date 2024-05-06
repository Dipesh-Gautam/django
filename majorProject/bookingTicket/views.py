from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
def index (request):
    book1 = Book()
    book1.price = 39
    book1.offer = True

    book2 = Book()
    book2.price = 55
    book2.offer = False

    book3 = Book()
    book3.price = 75
    book3.offer = True

    books = [book1, book2, book3]
    return render(request, 'index.html',{'books':books})