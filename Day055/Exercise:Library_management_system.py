"""
Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!
"""

class Library:
  def __init__(self):
    self.book = []
    self.genre = []
    self.noOfBooks = 0

  def addBooks(self,addedbook,addedgenre):
    self.book.append(addedbook)
    self.genre.append(addedgenre)
    self.noOfBooks = len(self.book)

  def removeBooks(self,removedbook):
    # Check if the book exists before removing
    if removedbook in self.book:
      removedGenreIndex = self.book.index(removedbook) # Get the index before removing
      self.book.remove(removedbook)
      poppedGenre = self.genre.pop(removedGenreIndex)
      self.noOfBooks -= 1 # Update book count after removing
    else:
      print("Book not found in the library.")

  def showInfo(self):
    print(f"The library currently has : {self.noOfBooks} books")


# Create the Library instance outside the loop
inpBook = Library() 
closed = False
while True:
  if closed:
    break
  # The outer loop now only runs if the user wants to access the library
  confirmation = input("Do you want to access your library? (Yes/No): ")
  if confirmation.capitalize() != "Yes":
    print("Thankyou.")
    break # Exit the outer loop if the user doesn't want to access the library

  while True:
    print("Processing...")
    ask = input("Press 1 if you want to add books to your library.\nPress 2 if you want to access any book from your library.\nEnter your choice : ")    
    match ask:
      case "1":
        inpBook.showInfo()
        enter = int(input("How many books do you want to add : "))
        for i in range(enter):
          inpgenre = input("Enter the genre of the book to be added: ")
          inputbook = input("Enter the name of the book to be added : ")
          inpBook.addBooks(inputbook,inpgenre)
        inpBook.showInfo()

      case "2":
        inpBook.showInfo()
        searchBook = input("Enter the name of the book you want to access : ")
        if searchBook in inpBook.book:
          print("Yes, book is present.")
          itemIndex = inpBook.book.index(searchBook)
          print(f"Selected book's genre is : {inpBook.genre[itemIndex]}")
          takeBook = input("Do you want to borrow the book ? : ")
          if (takeBook.capitalize() == "Yes"):
            print(f"Book taken by the user : {searchBook}")
            inpBook.removeBooks(searchBook) # Remove the book first
            inpBook.showInfo()
          else:
            pass
        else:
          print("Book not found in the library.")
      case _:
        print("Invalid Choice.")      

    # Ask if the user wants to access the library again after each interaction
    confirmation = input("Do you want to access your library again? (Yes/No): ")
    if confirmation.capitalize() != "Yes":
      print("Thankyou!")
      closed = True
      break
      # Exit the inner loop