from django.contrib import admin
from .models import BlogCount


@admin.register(BlogCount)
class BlogCountAdmin(admin.ModelAdmin):
    list_display = ['count']