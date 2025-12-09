'''
Docstring for blog.forms
'''
# Import necessary modules from Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Import Post model
from .models import Post # Import Post model for creating post forms

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
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post content here...'}),
        }
        