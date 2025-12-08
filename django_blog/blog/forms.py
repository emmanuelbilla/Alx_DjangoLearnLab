'''
Docstring for blog.forms
'''
# Import necessary modules from Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Import Post model
from .models import Post

# Define registration form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8}),
        }
        
    