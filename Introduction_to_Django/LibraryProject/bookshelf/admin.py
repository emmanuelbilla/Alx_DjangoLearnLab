from django.contrib import admin

# Register your models here.
from .models import Book # Import the Book model from .models
admin.site.register(Book) # Register the Book model with the admin site
