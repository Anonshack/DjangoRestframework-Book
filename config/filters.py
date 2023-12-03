from django_filters import rest_framework as filters
from .models import Books


class BookFilter(filters.FilterSet):
    class Meta:
        model = Books
        fields = {
            'title': ['contains'],
            'price': ['range'],
            'publish_date': ['exact'],
            'book_review': ['exact']
        }
