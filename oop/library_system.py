"""Module for representing Book Library."""


class Book:
    """class Representing Book"""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __del__(self):
        print(f"Deleting Book {self.title}")


class EBook(Book):
    """Docstring for EBook"""

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __del__(self):
        print(f"Deleting EBook {self.title}")


class PrintBook(Book):
    """
    Docstring for PrintBook
    """

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return (
            f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        )

    def __del__(self):
        print(f"Deleting PrintBook {self.title}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
