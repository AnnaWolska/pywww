from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Post, Category

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

@admin.register(Post)
class PostAdmin(ExportMixin,admin.ModelAdmin):
    list_display = ["title","content","published","created","modified","sponsored","user"]
    search_fields = ["title","content","published","created","modified","sponsored","user"]
    list_filter = ["published", "sponsored", "exemple_file", "tags"]
    autocomplete_fields = ['tags', 'categories']
    resource_class = PostResource

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "description"]
    search_fields = ["name"]
    # autocomplete_fields = ['tags', 'categories']
    # resource_class = PostResource


