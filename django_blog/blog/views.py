from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegistrationForm as RegisterForm
from .models import Post
from django.contrib.auth.models import User


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # email and password handled securely
            login(request, user)  # auto-login after registration
            messages.success(request, "Registration successful!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == "POST":
        user = request.user
        email = request.POST.get("email")
        if email:
            user.email = email
            user.save()
            messages.success(request, "Profile updated successfully.")
    return render(request, "blog/profile.html")

def home_view(request):
    return render(request, "blog/home.html")

# View to list blog posts
def post_list(request):
    # Logic to retrieve and display blog posts would go here
    return render(request, "blog/post_list.html")