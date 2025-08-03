# programming_paradigm/library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list of books

    def add_book(self, book):
        """Adds a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds the book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is either not in the library or already checked out.")

    def return_book(self, title):
        """Finds the book by title and returns it."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' was not checked out or does not exist in the library.")

    def list_available_books(self):
        """Prints all available books in the library."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books are currently available.")
        for book in available:
            print(book)
