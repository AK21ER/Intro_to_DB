# library_management.py

class Book:
    """Represents a book with title, author, and its checkout status."""

    def __init__(self, title, author):
        """Initialize book with title and author; default to available."""
        self.title = title  #thse title and the author are the attributes of the class which are public
        self.author = author
        self._is_checked_out = False  # private attribute since it is not in the parameter list this makes it to be private value and in order to modify it we need a method which access it

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # private list to hold Book instances

    def add_book(self, book): # so here is where the library class and the book class connected as the book is a paramater given to the add funnction which add books as there book class format like the title and author as a one
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # book not found or not available

    def return_book(self, title):
        """Return a book by title, making it available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # book not found or wasn't checked out

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
