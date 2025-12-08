"""
Urls for the blog app.
"""
# Import necessary modules
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#Define URL patterns
urlpatterns = [
    # Registration URL
    path('register/', views.register_view, name='register'),

    # Login URL
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Profile URL
    path('profile/', views.profile_view, name='profile'),

    # Home URL
    path('', views.home_view, name='home'),

    # Post detail URL
    path('post/', views.post_list, name='posts'),
    
]