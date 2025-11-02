 #Retrieve Operation

In [4]: for book in Book.objects.all().values():
   ...:     print(book)
   ...:
{'id': 3, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1958}