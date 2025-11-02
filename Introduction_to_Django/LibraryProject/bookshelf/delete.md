 #Delete Operation

In [35]: from bookshelf.models import Book

In [36]: book = Book.objects.get(title="Nineteen Eighty-Four")

In [37]: book.delete() #Deletes the book
Out[37]: (1, {'bookshelf.Book': 1})

In [38]: Book.objects.all()
Out[38]: <QuerySet []> 