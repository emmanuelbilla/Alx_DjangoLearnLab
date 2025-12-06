from django.shortcuts import render

# Create your views here.

'''Creating BookList view that extends the rest_framework.generics.ListAPIView.
Use the BookSerializer to serialize the data and the Book model as the queryset.
'''
#Importing necessary modules and classes
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

#Adding authentication and permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#Defining the BookList view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  #Queryset to retrieve all Book objects
    serializer_class = BookSerializer  #Serializer class to convert Book objects to JSON format

"""
Defining a BookViewSet that extends the rest_framework.viewsets.ModelViewSet and handles all CRUD operations for the Book model."""
#Importing necessary modules and classes
from rest_framework import viewsets

#Defining the BookViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  #Queryset to retrieve all Book objects
    serializer_class = BookSerializer  #Serializer class to convert Book objects to JSON format

# Adding authentication and permissions
    authentication_classes = [TokenAuthentication]  #Using TokenAuthentication for this viewset
    permission_classes = [IsAuthenticated]  #Restricting access to authenticated users only


