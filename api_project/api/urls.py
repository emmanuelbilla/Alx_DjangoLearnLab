"""
URL configuration for the project."""

'''
Including a URL pattern that routes to BookList view.'''
# Import necessary modules
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter


#Define a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')



# Define URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)), #Including the router URLs
]