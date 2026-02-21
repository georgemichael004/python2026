# building a simple library system where users can borrow and return books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        self.is_borrowed = True
    
    def return_book(self):
        self.is_borrowed  = False
    
    def __str__(self):
        status = 'Borrowed' if self.is_borrowed else 'Available'
        return f"{status} | Title: {self.title} | Author: {self.author}"
    
        
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
    
    def list_books(self):
        if not self.books:
            print("The Library has no books.")
            return
        print("\nBooks in the Library:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def borrow_book(self, index):
        if not self.books:
            print("The library has no books.\n")
            return

        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.books):
            print("Invalid book number.\n")
            return

        book = self.books[actual_index]
        if book.is_borrowed:
            print("This book is already borrowed.\n")
        else:
            book.borrow()
            print(f"You borrowed '{book.title}'.\n")
        
        

        

    
    def return_book(self, index):
        if not self.books:
            print("The library has no books.\n")
            return

        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.books):
            print("Invalid book number.\n")
            return

        book = self.books[actual_index]
        if not book.is_borrowed:
            print("This book is not borrowed yet.\n")
        else:
            book.return_book()
            print(f"You returned '{book.title}'.\n")

        
class Member:
    def __init__(self, name):
        self.name = name
        
    def borrow_from_library(self, library, index):
        library.borrow_book(index)
    
    def return_to_library(self,library, index):
        library.return_book(index)


lib = Library()
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("Clean Code", "Robert Martin"))

m = Member("George")

lib.list_books()
m.borrow_from_library(lib, 2)
lib.list_books()
m.return_to_library(lib, 2)
lib.list_books()
