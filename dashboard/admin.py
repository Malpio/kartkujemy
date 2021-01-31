from django.contrib import admin
from dashboard.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register your models here.
