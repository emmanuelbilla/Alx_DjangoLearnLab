"""
Urls for the blog app.
"""
# Import necessary modules
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#Required imports for CRUD operations on blog posts
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


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

    # CRUD URLs for blog posts
    path('posts/', PostListView.as_view(), name='posts'), # List view for posts
    path('posts/new/', PostCreateView.as_view(), name='post-create'), # Create view for a new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # Detail view for a single post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'), # Update view for a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete view for a post

    
]