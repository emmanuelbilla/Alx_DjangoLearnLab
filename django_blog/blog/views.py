from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegistrationForm as RegisterForm
from .models import Post
from django.contrib.auth.models import User

# View imports for post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm



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

'''
Class based Views for blog posts
'''
# List view for posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 8

# Detail view for a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create view for new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update view for existing post. Only the author can update.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete view for a post. Only the author can delete.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# View to add a comment to a post as a fbv
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return redirect('post_detail', pk=post.id)

# Update view for existing comment. Only the author can update.
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_edit.html'

    # Ensure the comment author is the logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Test function to ensure only the comment author can edit
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    # Define success URL after editing comment
    def get_success_url(self):
        return self.object.post.get_absolute_url()

# Delete view for a comment. Only the author can delete.
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    # Test function to ensure only the comment author can delete
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    # Define success URL after deleting comment
    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

