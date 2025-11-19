'''
Implements the librarian view for the library management application.
'''
# Importing necessary modules
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Function to check if the user is a librarian
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Librarian view protected by user_passes_test decorator
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})