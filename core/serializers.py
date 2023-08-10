from rest_framework import serializers

from core.models import Book, Reader, Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = '__all__'

    def create(self, validated_data):
        books_taken = validated_data.get('books_taken', [])
        for book in books_taken:
            if book.available_amount <= 0:
                raise serializers.ValidationError("Читатель может брать только книги, которые есть в наличии.")
        if len(books_taken) > 3:
            raise serializers.ValidationError("Читатель не может брать больше 3-х книг!")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        books_taken = validated_data.get('books_taken', [])
        for book in books_taken:
            if book.available_amount <= 0:
                raise serializers.ValidationError("Читатель может брать только книги, которые есть в наличии.")
        if len(books_taken) > 3:
            raise serializers.ValidationError("Читатель не может брать больше 3-х книг!")
        return super().update(instance, validated_data)


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

