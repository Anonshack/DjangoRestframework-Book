from rest_framework import serializers
from .models import Auther, Books, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class AutherListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Auther
        fields = ['id', 'name', 'age', 'biography', 'author_name']


class AutherDetailSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(many=True, source='book_auther')

    class Meta:
        model = Auther
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    auther = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    auther = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True, source='book_review')
    reviews_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = '__all__'

    def get_reviews_count(self, objects):
        reviews_count = objects.book_review.count()
        return reviews_count

    def get_avg_rate(self, objects):
        reviews = objects.book_review.all()
        return sum(review.rate for review in reviews) / len(reviews) if reviews else 0