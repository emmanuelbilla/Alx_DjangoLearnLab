''' Implements the member view for the library management application.'''

# Importing necessary modules
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Function to check if the user is a member
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Member view protected by user_passes_test decorator
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})