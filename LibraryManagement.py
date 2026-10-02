class Library:

    def __init__(self, id, name, author, avlbl):
        self.book_id= id
        self.book_name= name
        self.book_author = author
        self.is_available = avlbl

    def display_book_details(self):
        print("----Book Details----")
        print("Book ID : ", self.book_id)
        print("Book Name : ", self.book_name)
        print("Author : ", self.book_author)
        print("Availability : ", self.is_available)

    def checkAvailability(self):
        if self.is_available:
            print("Book is AVAILABLE")
        else:
            print("Book is NOT available")

    def issue(self):
        if self.is_available == False:
            print("Book is already ISSUED")
        else:
            self.is_available = False
            print("Book issue successful")

    def return_book(self):
        if self.is_available == True:
            print("Book is already available. Cannot be returnned")
        else:
            self.is_available = True
            print("Book has been succesfully returned")

book = Library(101, "Python Programming", "John Smith", True)

# book.display_book_details()

book.issue()

book.issue()

book.return_book()
book.checkAvailability()
        