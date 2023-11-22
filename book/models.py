from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class BorrowedBook(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='books')
    borrower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='borrowers')
    borrow_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.borrower.username} borrowed book {self.book.title}"
