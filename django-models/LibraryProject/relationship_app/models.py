from django.db import models

# Models for relationship_app.

# For Author
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# For Book
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    
# For Library
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# For Librarian
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

''' 
Creating the UserProfile model to demonstrate OneToOne relationship with Django's built-in User model. 
'''

# Importing User model
from django.contrib.auth.models import User
from django.db.models.signals import post_save # To create UserProfile on User creation
from django.dispatch import receiver # To handle signals

class UserProfile(models.Model): # Extending User model with OneToOne relationship
    Role_CHOICES = [
        ('admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    # OneToOne relationship with User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # UserProfile linked to User
    role = models.CharField(max_length=20, choices=Role_CHOICES, default='Member') # Role field with choices

    def __str__(self): # String representation of UserProfile
        return f"{self.user.username} - {self.role}"
    
# Signal to create or update UserProfile when User is created or updated
@receiver(post_save, sender=User) # Listening to User model's post_save signal
def create_user_profile(sender, instance, created, **kwargs): # Function to create UserProfile
    if created: # If User is created
        UserProfile.objects.create(user=instance) # Create UserProfile
    instance.profile.save() # Save UserProfile on User update
@receiver(post_save, sender=User) # Listening to User model's post_save signal
def save_user_profile(sender, instance, **kwargs): # Function to save UserProfile
    instance.profile.save() # Save UserProfile on User update

    
