from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Writer, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name',)


class WriterSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Writer
        fields = ('id', 'name', 'books',)

