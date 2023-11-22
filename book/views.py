from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Author, Book, BorrowedBook
from .serializers import BookSerializer, AuthorSerializer, BorrowedBookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ListAllAvailableBooks(ListAPIView):
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'published_date']

    def get_queryset(self):
        qs = Book.objects.filter(is_available=True)
        return qs


class BorrowBookAPIView(ListCreateAPIView):
    serializer_class = BorrowedBookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        borrowed_books = BorrowedBook.objects.filter(
            borrower=self.request.user)
        return borrowed_books
