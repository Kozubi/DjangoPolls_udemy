from django.shortcuts import render, HttpResponse

from .models import Author, Book

# Create your views here.

def index(req, book):
    print("Book is ", book)
    return HttpResponse(str(book))