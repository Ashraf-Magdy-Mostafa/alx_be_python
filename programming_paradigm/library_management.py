class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            print(f"'{self.title}'  is already cheked out.")
            return False
        
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            print(f"'{self.title}' is already in the library.")
            return False
    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f'Book(title="{self.title}", author="{self.author}")'


class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)

    def check_out_book(self,title):
        book = next((b for b in self._books if b.title == title), None)
        if book :
            if book.check_out() :
                print(f"Checked out: {title}")
        else:
            print(f"Error: Book with title '{title}' not found in the library.")
    
    def return_book(self,title):
        book = next((b for b in self._books if b.title == title), None)
        if book:
            if book.return_book():
                print(f"Returned: {title}")
        else:
            print(f"Error: Book with title '{title}' not found in the library.")

    def list_available_books(self):
        # loop and return books that is available (if is available is true)
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
    




if __name__ == "__main__":
     # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()