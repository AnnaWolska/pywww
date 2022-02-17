from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from books.models import Books
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from tags.models import Tag
from books.forms import BookForm


def library(request):
    books = Books.objects.all()
    context = {'books' : books}
    return render(request, "books.html", context)


def book_details(request, book_id):
    book = Books.objects.get(pk=book_id)
    title = book.title
    decription = book.decription
    author = book.author
    tags = book.tags
    return render(request, "details.html", context = {
        'title' : title,
        'decription': decription,
        'author' : author,
        'tags' : tags,
    })


def add_book(request):
    # form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("books:add_book"))
    else:
        form = BookForm()
    return(
        render(request, "add_book.html", {"form":form})
    )
