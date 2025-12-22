# Book class definition
class Book:
    
    # Initialise the attributes of class 
    def __init__(self, book_id, b_title, b_author):
        self.book_id = book_id          
        self.b_title = b_title          
        self.b_author = b_author        
        self.is_available = True   # Book is available initially

    # Method to issue the book
    def issue_book(self):
        if self.is_available:           # Checks if book is available
            self.is_available = False   # If True Updates book as issued
            print(f"{self.b_title} book issued successfully")
        else:
            print(f"{self.b_title} book already issued")  # Cannot issue again once book is issued(until returned)

    # Method to return the book
    def return_book(self):
        if not self.is_available:       # Checks if book is already issued
            self.is_available = True    # If True Updates book as available
            print(f"{self.b_title} book returned successfully")
        else:
            print(f"{self.b_title} book was not issued")  # Prevent invalid return

    # Method to display current book status
    def display_status(self):
        if self.is_available:
            print(f"{self.b_title} book status: Available")
        else:
            print(f"{self.b_title} book status: Issued")


# Creating a Book object
b1 = Book("B1", "Wings of Fire", "A.P.J Abdul Kalam")

b1.display_status()   # Initial status of book
b1.issue_book()   # Book issued
b1.issue_book()   #for better understanding check again if book can be re-issued
b1.return_book()   #returns the book
b1.display_status()  # Final status of the book
