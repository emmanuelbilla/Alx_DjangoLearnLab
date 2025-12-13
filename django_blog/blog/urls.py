"""
Urls for the blog app.
"""
# Import necessary modules
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#Required imports for CRUD operations on blog posts
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView


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
    path('post/new/', PostCreateView.as_view(), name='post-create'), # Create view for a new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # Detail view for a single post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update view for a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete view for a post

    #URLs for comments are added here
    path('post/<int:pk>/comment/', views.add_comment, name='add-comment'), # Add comment to a post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'), # Create comment view
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'), # Edit comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'), # Delete comment
    path('search/', views.search_posts, name='search'), # Search posts
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(),name='posts_by_tag'), # View posts by tag

    
]