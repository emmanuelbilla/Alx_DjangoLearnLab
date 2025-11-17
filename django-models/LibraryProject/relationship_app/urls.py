'''Description of code:
Django URL configuration for relationship app managing book and library views.'''

from django.urls import path # Importing path function to define URL patterns
from .views import list_books, library_detail # Importing views for handling requests

app_name = 'relationship_app' # Setting application namespace for URL namespacing

# Defining URL patterns for the relationship app
urlpatterns = [
    path('books/', list_books, name='list_books'), # URL pattern for listing books
    path('library/<int:pk>/', library_detail.as_view(), name='library_detail'), # URL pattern for library detail view
]