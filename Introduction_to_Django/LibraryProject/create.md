#Code:
#To make use of the Book class which allows the creation of the book records, the bookshelf model has to be imported. 
In [1]: from bookshelf.models import Book

#Next a book instace was created with the description in the class variable. 
In [2]: book = Book(title= "1984", author= "George Orwell", publication_year
   ...: = 1949)

#The the save function was called for the book instance using book.save
In [3]: book.save()

#Results
#To confirm the creation of the book instance it was called to output
In [4]: print(book)
1984