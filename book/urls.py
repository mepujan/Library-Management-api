from django.urls import path
from .views import AuthorListCreateAPIView, ListAllAvailableBooks, BorrowBookAPIView


urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='authors'),
    path('books/', ListAllAvailableBooks.as_view(), name='books'),
    path('borrowed_book/', BorrowBookAPIView.as_view(), name='borrowed_book')
]
