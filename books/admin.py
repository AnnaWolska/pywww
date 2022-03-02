from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Books, Borrow


class BooksResource(resources.ModelResource):
    class Meta:
        model = Books

@admin.register(Books)
class BooksAdmin(ExportMixin,admin.ModelAdmin):
    list_display = ["id", "title", "decription", "available", "publication_year", "author"]
    search_fields = ["title", "author", "publication_year", "available", "tags"]
    list_filter = ["author", "available", "tags"]
    autocomplete_fields = ['tags']
    resource_class = BooksResource

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ["book", "user", "borrow_date", "return_date"]
    search_fields = ["book", "user", "borrow_date", "return_date"]
    list_filter = ["book", "user", "borrow_date", "return_date"]
    resource_class = BooksResource
