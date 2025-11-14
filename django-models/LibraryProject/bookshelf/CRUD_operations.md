from bookshelf.models import Book
In [1]: #Create Operation

In [2]: book = Book.objects.create( title= "1984", author = "George Orwell", publi
   ...: cation_year = 1958 )

In [3]: #Retrieve Operation

In [4]: for book in Book.objects.all().values():
   ...:     print(book)
   ...:
{'id': 3, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1958}

In [5]: #Alternate retrieval method

In [6]: book = Book.objects.get(title = "1984")

In [7]: book.title, book.author, book.publication_year
Out[7]: ('1984', 'George Orwell', 1958)

In [8]: #Update Operation

In [9]: book = Book.objects.get(title="1984")

In [10]: book.title = "Nineteen Eighty-Four" #Modifies the name to new name

In [11]: print(book.title) #Confirm the change
Nineteen Eighty-Four

In [12]: book.save() #Saves changes

In [13]: #Delete Operation

In [14]: book = Book.objects.get(title="Nineteen Eighty-Four")

In [15]: book.delete()
Out[15]: (1, {'bookshelf.Book': 1})

In [16]: Book.objects.all() #To confirm deletion
Out[16]: <QuerySet []>

In [17]: #Missing in the first line is the command - "from bookshelf.models import Book"