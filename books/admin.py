from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Books, Borrow, Author


class BooksResource(resources.ModelResource):
    class Meta:
        model = Books


@admin.register(Books)
class BooksAdmin(ExportMixin,admin.ModelAdmin):
    list_display = ["id", "title", "decription", "available", "publication_year", "author", "tags_count"]
    search_fields = ["title", "publication_year", "available", "tags"]
    list_filter = ["available", "tags"]
    autocomplete_fields = ['tags']
    resource_class = BooksResource
    #
    # def tags_count(self, obj):
    #     return obj.tags.count


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ["book", "user", "borrow_date", "return_date"]
    search_fields = ["book", "user", "borrow_date", "return_date"]
    list_filter = ["book", "user", "borrow_date", "return_date"]
    resource_class = BooksResource

#
# class AuthorResource(resources.ModelResource):
#     class Meta:
#         model = Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "birth_year", "death_year", "biogram"]
    search_fields = ["name", "birth_year", "death_year", "biogram"]
    list_filter = ["name", "birth_year", "death_year", "biogram"]
    resource_class = BooksResource