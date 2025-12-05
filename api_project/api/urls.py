"""
URL configuration for the project."""

'''
Including a URL pattern that routes to BookList view.'''
# Import necessary modules
from django.urls import path
from .views import BookList

# Define URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]