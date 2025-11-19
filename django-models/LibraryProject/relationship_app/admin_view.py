''' Implements the admin view for managing Library. 
    - Customizes the admin interface for the Library model.'''

# Importing necessary modules
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Function to check if the user is an admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin view protected by user_passes_test decorator
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})  