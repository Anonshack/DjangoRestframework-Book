from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import filters
from .filters import BookFilter
from .serializers import AutherListSerializer, AutherDetailSerializer, BookListSerializer, BookDetailSerializer
from .models import Auther, Books


class AutherListAPI(generics.ListAPIView):
    serializer_class = AutherListSerializer
    queryset = Auther.objects.all()
    filter_backends = [DjangoFilterBackend]


class AutherDetailAPI(generics.RetrieveAPIView):
    serializer_class = AutherDetailSerializer
    queryset = Auther.objects.all()
    filter_backends = [DjangoFilterBackend]


class BookListAPI(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Books.objects.all()
    filter_backends = [DjangoFilterBackend]
    search_fields = ['title']
    ordering_fields = ['price']
    filterset_class = BookFilter


class BookDetailAPI(generics.RetrieveAPIView):
    serializer_class = BookDetailSerializer
    queryset = Books.objects.all()
