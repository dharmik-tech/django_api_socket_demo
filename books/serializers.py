from django.utils import timezone
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value < 1000 or value > current_year:
            raise serializers.ValidationError('Publication Year is invalid.')
        return value
