 'Defining a BookSerializer class which would extend rest_framework.serializers.ModelSerializer and include all fields of the Book model.'

#importing necessary modules
from rest_framework import serializers
from .models import Book

# Defining the BookSerializer class
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
