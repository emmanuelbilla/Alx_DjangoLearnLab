 #Update Operation

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four" #Modifies the name to new name

print(book.title) #Confirm the change

#Output
Nineteen Eighty-Four

book.save() #Saves changes