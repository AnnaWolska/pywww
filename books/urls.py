from django.urls import path
from books.views import library, book_details, add_book, borrow_books

app_name = "books"
urlpatterns = [
    path('',library, name="list"),
    path('<int:book_id>', book_details, name="details"),
    path('add',add_book, name="add_book"),
    path('<int:book_id>/borrows', borrow_books, name="borrows"),
    path('borrow_list', borrow_books, name="borrow_list")
]