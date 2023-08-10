from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Book, Reader, Author
from core.serializers import BookSerializer, ReaderSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(available_amount__gt=0)
    serializer_class = BookSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
