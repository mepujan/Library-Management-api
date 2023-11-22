from rest_framework import serializers
from .models import Author, Book, BorrowedBook


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BorrowedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = BorrowedBook
        fields = ('book', 'borrower', 'borrow_date', 'return_date')
