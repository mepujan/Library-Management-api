from django.contrib import admin
from .models import Author, Book, BorrowedBook


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BorrowedBook)
