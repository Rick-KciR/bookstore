from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .form import BookForm


def index(request):
    return render(request, "book_store_app/index.html", {})


def about(request):
    return render(request, "book_store_app/about.html", {})

def create_book(request):
    data = {}
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_booklist")
    data["form"] = form
    return render(request, "book_store_app/login.html", data)


def book_list(request):
    data = {"Book": Book.objects.all()}
    return render(request, "book_store_app/book_list.html", data)


def update(request, pk):
    data = {}
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect("url_booklist")

    data["form"] = form
    data["book"] = book
    return render(request, "book_store_app/login.html", data)


def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("url_booklist")

