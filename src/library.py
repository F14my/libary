from src.collections.book_collection import BookCollection
from src.collections.book_index import BookIndex
from src.models import Book


class Library:
    def __init__(self):
        """
        Library constructor
        """
        self.book_collection = BookCollection()
        self.book_index = BookIndex()

    def add_book(self, book: Book) -> None:
        """
        Add a book to the library

        :param book: book to add
        :return: None
        """
        self.book_collection.add_book(book)
        self.book_index.add_book(book)

    def remove_book(self, book: Book) -> None:
        """
        Remove a book from the library

        :param book: book to remove
        :return: None
        """
        self.book_collection.remove_book(book)
        self.book_index.remove_book(book)

    def get_all_books(self) -> BookCollection:
        """
        Get all books in the library

        :return: all books from the library(BookCollection)
        """
        return self.book_collection

    def find_by_isbn(self, isbn: int) -> Book:
        """
        Find a book by ISBN

        :param isbn: isbn of the book to find
        :return: book
        """
        return self.book_index.find_by_isbn(isbn)

    def find_by_author(self, author: str) -> list[Book]:
        """
        find all books by author

        :param author: author to find books by
        :return: books of this author
        """
        return self.book_index.find_by_author(author)

    def find_by_year(self, year: int) -> list[Book]:
        """
        find all books by year

        :param year: year to find books by
        :return: books of this year
        """
        return self.book_index.find_by_year(year)

    def __len__(self) -> int:
        """
        Get number of books in the library

        :return: length of the library
        """
        return len(self.book_collection)