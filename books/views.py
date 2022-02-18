from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from books.models import Books, Borrow
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from tags.models import Tag
from books.forms import BookForm, BookBorrowForm
from django.utils import  timezone

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
    form = BookBorrowForm()
    form.helper.form_action = reverse("books:borrows", args=[book.id])
    return render(request, "details.html", context = {
        'title' : title,
        'decription': decription,
        'author' : author,
        'tags' : tags,
        'book':book,
        "form":form
    })


def add_book(request):
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


def borrow_books(request, book_id=None):
    user = request.user
    if request.method == "POST":
        if user.is_authenticated:
            if request.POST.get("borrow"):
                book = Books.objects.get(pk=book_id)
                Borrow.objects.create(
                    user=user,
                    book=book
                )
                book.available = False
                book.save()
                return HttpResponseRedirect(reverse("books:details", args=[book_id]))
            else:
                keys = [key for key in request.POST.keys() if key.startswith("book_")]
                key=int(keys[0].split("_")[1])
                book = Borrow.objects.get(pk=key)
                borrow = Borrow.objects.filter(user=user, book=book).last()
                if not borrow.return_date:
                    borrow.return_date = timezone.now()
                    borrow.save()
                    book.available = True
                    book.save()
                return HttpResponseRedirect(reverse("books:boorow_list"))

    else:
        borrows = Borrow.objects.filter(user=user)
        return render(request, "books/borrow_list", {"borrows":borrows})