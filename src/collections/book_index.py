from src.models import Book


class BookIndex:
    def __init__(self):
        self.by_isbn = {}
        self.by_author = {}
        self.by_year = {}

    def add_book(self, book: Book) -> None:
        """
        Method to add a book to the collection(dictionary)

        :param book: Book to add
        :return: None
        """
        self.by_isbn[book.isbn] = book
        if book.author not in self.by_author:
            self.by_author[book.author] = []
        self.by_author[book.author].append(book)
        if book.year not in self.by_year:
            self.by_year[book.year] = []
        self.by_year[book.year].append(book)

    def remove_book(self, book: Book) -> None:
        """
        Method to remove a book from the collection(dictionary)

        :param book: Book to remove
        :return: None
        """
        if book.isbn in self.by_isbn:
            del self.by_isbn[book.isbn]

        if book.author in self.by_author:
            if book.year in self.by_year[book.year]:
                self.by_author[book.author].remove(book)
            if not self.by_author[book.author]:
                del self.by_author[book.author]

        if book.year in self.by_year:
            if book in self.by_year[book.year]:
                self.by_year[book.year].remove(book)
            if not self.by_year[book.year]:
                del self.by_year[book.year]

    def find_by_isbn(self, isbn: int) -> Book:
        """
        Method to find a book from the collection(dictionary)

        :param isbn: ISBN of the book to find
        :return: Book
        """
        return self.by_isbn.get(isbn)

    def find_by_author(self, author: str) -> list[Book]:
        """
        Method to find a book from the collection(dictionary)

        :param author: author of the book to find
        :return: list of Books from this author
        """
        return self.by_author.get(author)

    def find_by_year(self, year: int) -> list[Book]:
        """
        Method to find a book from the collection(dictionary)

        :param year: year of the book to find
        :return: list of Books from this year
        """
        return self.by_year.get(year)
