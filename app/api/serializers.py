from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Writer, Book


class BookInfoSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('name',)


class WriterSerializer(ModelSerializer):
    book = BookInfoSerializer(
        source='books',
        many=True,
        read_only=True,
    )
    class Meta:
        model = Writer
        fields = ('id', 'name', 'book')

