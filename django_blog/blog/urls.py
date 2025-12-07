"""
Urls for the blog app.
"""
# Import necessary modules
from django.urls import path
from django.contrib.auth import views as auth_views

#Define URL patterns
urlpatterns = [
    # Login URL
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    
]