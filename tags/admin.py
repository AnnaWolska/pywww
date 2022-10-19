from django.contrib import admin

from galleries.admin import PhotoInLine
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug",]
    search_fields = ["name",]
    #
    # def tags_count(self, obj):
    #     return obj.name.count