from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "bio"]
    search_fields = ["id", "user", "bio"]
