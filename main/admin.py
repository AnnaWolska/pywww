from django.contrib import admin
from .models import UserProfile


admin.site.site_header = "PyWWW Admin"
admin.site.site_title = "PyWWW Admin Portal"
admin.site.index_title = "Witaj w Portalu PyWWW"


@admin.register(UserProfile)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "bio"]
    search_fields = ["id", "user", "bio"]
