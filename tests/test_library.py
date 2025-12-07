import pytest

from src.models import Book
from src.library import Library

@pytest.fixture
def sample_books() -> list[Book]:
    """The list of Book objects to test"""
    return [
        Book(title="Преступление и наказание", author="Фёдор Достоевский",
             year=1866, genre="Роман", isbn=1111111111111),
        Book(title="Идиот", author="Фёдор Достоевский",
             year=1869, genre="Роман", isbn=2222222222222),
        Book(title="Война и мир", author="Лев Толстой",
             year=1869, genre="Роман-эпопея", isbn=3333333333333),
        Book(title="Анна Каренина", author="Лев Толстой",
             year=1877, genre="Роман", isbn=4444444444444),
    ]


@pytest.fixture
def library(sample_books: list[Book]) -> Library:
    """Library with a books"""
    lib = Library()
    for book in sample_books:
        lib.add_book(book)
    return lib


def test_book_fields():
    book = Book(
        title="Тестовая книга",
        author="Тестовый Автор",
        year=2024,
        genre="Тестовый жанр",
        isbn=1234567890123,
    )

    assert book.title == "Тестовая книга"
    assert book.author == "Тестовый Автор"
    assert book.year == 2024
    assert book.genre == "Тестовый жанр"
    assert book.isbn == 1234567890123


def test_library_add_book_increases_count(library: Library):
    initial_count = len(library.get_all_books())
    new_book = Book(
        title="Новая книга",
        author="Новый Автор",
        year=2020,
        genre="Фантастика",
        isbn=9999999999999,
    )

    library.add_book(new_book)

    books = library.get_all_books()
    assert len(books) == initial_count + 1
    assert any(b.isbn == new_book.isbn for b in books)


def test_library_remove_book_decreases_count(library: Library):
    books_before = library.get_all_books()
    initial_count = len(books_before)
    book_to_remove = books_before[0]

    library.remove_book(book_to_remove)

    books_after = library.get_all_books()
    assert len(books_after) == initial_count - 1
    assert all(b.isbn != book_to_remove.isbn for b in books_after)


def test_library_get_all_books_is_iterable(library: Library):
    books = library.get_all_books()
    titles = [book.title for book in books]
    assert "Преступление и наказание" in titles
    assert "Война и мир" in titles


def _to_list(result):
    """
    Utilit function to convert result into a list of books
    """
    if result is not None:
        if isinstance(result, list):
            return result
        return list(result)
    return []


def test_find_by_author_returns_correct_books(library: Library):
    res = library.find_by_author("Фёдор Достоевский")
    result_books = _to_list(res)

    assert len(result_books) == 2
    titles = {b.title for b in result_books}
    assert "Преступление и наказание" in titles
    assert "Идиот" in titles


def test_find_by_year_returns_correct_books(library: Library):
    res = library.find_by_year(1869)
    result_books = _to_list(res)

    assert len(result_books) == 2
    titles = {b.title for b in result_books}
    assert "Идиот" in titles
    assert "Война и мир" in titles


def test_find_by_isbn_returns_single_book(library: Library, sample_books: list[Book]):
    target = sample_books[2]
    found = library.find_by_isbn(target.isbn)

    assert isinstance(found, Book)
    assert found.title == "Война и мир"
    assert found.author == "Лев Толстой"


def test_find_by_isbn_not_found_returns_none(library: Library):
    found = library.find_by_isbn(9999999999999)
    assert found is None


def test_indexes_update_on_remove(library: Library, sample_books: list[Book]):
    book_to_remove = sample_books[0]
    author = book_to_remove.author
    year = book_to_remove.year
    isbn = book_to_remove.isbn

    by_author_before = _to_list(library.find_by_author(author))
    assert any(b.isbn == isbn for b in by_author_before)

    by_year_before = _to_list(library.find_by_year(year))
    assert any(b.isbn == isbn for b in by_year_before)

    assert library.find_by_isbn(isbn) is not None

    library.remove_book(book_to_remove)

    by_author_after = _to_list(library.find_by_author(author))
    assert all(b.isbn != isbn for b in by_author_after)

    by_year_after = _to_list(library.find_by_year(year))
    assert all(b.isbn != isbn for b in by_year_after)

    assert library.find_by_isbn(isbn) is None
