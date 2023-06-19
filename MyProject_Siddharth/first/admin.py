# Register your models here.
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'Auth_first_name', 'Auth_email', 'Title', 'Publisher', 'Publication_Year', 'Issue_Status', 'Issued_Roll_No')


admin.site.register(Book, BookAdmin)
