 #Retrieve Operation

book = Book.objects.get(title = "1984")

In [7]: book.title, book.author, book.publication_year
Out[7]: ('1984', 'George Orwell', 1958)