from src.models import Book

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        """
        Method to add a book to the collection

        :param book: Book to add
        :return: None
        """
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        """
        Method to remove a book from the collection

        :param book: Book to remove
        :return: None
        """
        if book in self.books:
            self.books.remove(book)

    def __len__(self) -> int:
        """
        Method to return the number of books in the collection

        :return: int - number of books in the collection
        """
        return len(self.books)

    def __iter__(self):
        """
        Method to iterate through the collection
        """
        return iter(self.books)

    def __getitem__(self, idx: int) -> Book | list[Book]:
        """
        Method to get a book from the collection

        :param idx: index of the book to get
        :return: book or list[Book]
        """
        return self.books[idx]
