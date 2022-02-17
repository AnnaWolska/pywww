from django.urls import path
from books.views import library, book_details, add_book

app_name = "books"
urlpatterns = [
    path('',library, name="list"),
    path('<int:book_id>', book_details, name="details"),
    path('add',add_book, name="add_book")
]