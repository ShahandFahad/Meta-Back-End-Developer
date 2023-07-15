from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fileds = ["id", "title", "author", "price"] # Depricated
        fields = "__all__"
