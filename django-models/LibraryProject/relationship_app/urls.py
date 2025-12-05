'''Description of code:
    -Django URL configuration for relationship app managing book and library views.
'''

from django.urls import path # Importing path function to define URL patterns
from .views import list_books, library_detail # Importing views for handling requests
from django.contrib.auth import views as auth_views # Importing Django's built-in authentication views
from .views import register # Importing custom user registration view
from . import views # Importing views module for additional view functions

# Importing additional views for RBAC (Role-Based Access Control)
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

app_name = 'relationship_app' # Setting application namespace for URL namespacing

# Defining URL patterns for the relationship app
urlpatterns = [
    path('books/', list_books, name='list_books'), # URL pattern for listing books
    path('library/<int:pk>/', library_detail.as_view(), name='LibraryDetailView'), # URL pattern for library detail view
    path('register/', views.register, name='register'), # URL pattern for user registration
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'), # URL pattern for user login
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), # URL pattern for user logout

    # URL patterns for role-based access control views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'), 

    #Additional URL patterns for adding, editing, and deleting books
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]