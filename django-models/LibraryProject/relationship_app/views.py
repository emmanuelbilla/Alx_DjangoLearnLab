from django.shortcuts import render

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
    