from django.shortcuts import render, redirect

# Importing the necessary model
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView


'''
Creating a function-based view in relationship_app/views.py:
    - That lists all books stored in the database.
    - The view also renders a simple text list of book titles and their authors.
    '''
def list_books(request):
    # Fetching all Book objects from the database
    books = Book.objects.all()
    
    # Creating a context dictionary to pass to the template
    context = {
        'list_books': books
    }
    
    # Rendering the template with the list of books
    return render(request, 'relationship_app/list_books.html', context)


''' 
Creating a class-based view in relationship_app/views.py that:
    - Displays details for a specific library.
    - Listing all books available in that library.
    - Utilize Django’s ListView or DetailView to structure this class-based view.
    '''
class library_detail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding the list of books in the library to the context
        context['books'] = self.object.books.all()
        return context
    
''' 
Creating user registration and authentication views in relationship_app/views.py:
    - Allow new users to register.
    - Handle user login and logout functionalities.
    - Utilize Django’s built-in authentication views and forms where appropriate.
'''
# Authentication Views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST': # Handling form submission
            form = UserCreationForm(request.POST) # Creating a form instance with POST data
            if form.is_valid(): # Validating the form
                user = form.save()
                login(request, user)
                return redirect('list_books') # Redirecting to the book list after successful registration
            
    else: # Displaying the registration form
            form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

    ''' Creating RBAC views in relationship_app/views.py:'''

    # Importing necessary modules not previously imported
    from django.contrib.auth.decorators import user_passes_test

    # Role check function
    def is_admin(user):
         return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'
    
    def is_librarian(user):
         return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'
    
    def is_member(user):
         return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'
    
    # Admin-only view
    @user_passes_test(is_admin)
    def admin_view(request):
        return render(request, 'relationship_app/admin_view.html')
    
    # Librarian-only view
    @user_passes_test(is_librarian)
    def librarian_view(request):
        return render(request, 'relationship_app/librarian_view.html')
    
    # Member-only view
    @user_passes_test(is_member)
    def member_view(request):
        return render(request, 'relationship_app/member_view.html')
    
''' Creating permissions to add_book, edit_book, and delete_book views in relationship_app/views.py'''

#Importing necessary modules not previously imported
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required

# View to add a book
@permission_required('relationship_app.can_add_book', raise_exception=True) 
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        # Assuming Author model is imported
        author = get_object_or_404(Author, id=author)
        Book.objects.create(title=title, author=author)
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author = request.POST.get('author')
        book.author = get_object_or_404(Author, id=author)
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})