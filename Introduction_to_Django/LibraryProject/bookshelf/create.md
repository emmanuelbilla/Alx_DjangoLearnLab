#Code:
#To make use of the Book class which allows the creation of the book records, the bookshelf model has to be imported. 
In [1]: from bookshelf.models import Book

#Next a book instace was created with the description in the class variable. 
#Create Operation

In [2]: book = Book.objects.create( title= "1984", author = "George Orwell", publi
   ...: cation_year = 1958 )

#Results
#To confirm the creation of the book instance it was called to output
In [3]: print(book)
1984