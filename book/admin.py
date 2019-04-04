from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'author', 'created_date']
    list_display_links = ['name', 'author']
    list_filter = ['created_date', 'page_count']
    class Meta:
        model = Book

admin.site.register(Book, BookAdmin)