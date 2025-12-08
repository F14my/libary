from src.library import Library
import random

from src.models import RareBook, Book, DigitalBook
from src.constants import TITLES, AUTHORS, GENRES


def generate_book() -> Book:
    """
    Generate a random book

    :return: random book
    """
    title = random.choice(TITLES)
    author = random.choice(AUTHORS)
    genre = random.choice(GENRES)
    year = random.randint(1800, 2024)
    isbn = int("".join(str(random.randint(0, 9)) for _ in range(13)))

    kind_roll = random.randint(0, 9)

    if kind_roll >= 8:
        price = random.randint(10_000, 200000)
        rarity_level = random.randint(6, 10)
        return RareBook(
            title=title,
            author=author,
            year=year,
            genre=genre,
            isbn=isbn,
            price=price,
            rarity_level=rarity_level,
        )
    elif kind_roll >= 6:
        file_format = random.choice(["PDF", "EPUB", "FB2", "MOBI"])
        pages = random.randint(50, 1200)
        return DigitalBook(
            title=title,
            author=author,
            year=year,
            genre=genre,
            isbn=isbn,
            file_format=file_format,
            pages=pages,
        )
    else:
        return Book(
            title=title,
            author=author,
            year=year,
            genre=genre,
            isbn=isbn,
        )


def event_add_book(library: Library) -> None:
    """
    Add a book to the library

    :param library: library
    :return: None """
    book = generate_book()
    library.add_book(book)
    print(
        f"[ADD] Добавлена книга: {book.get_description()}"
    )

def event_remove_random_book(library: Library) -> None:
    """
    remove a random book
    :param library: library
    :return: None
    """
    books = library.get_all_books()
    if len(books) == 0:
        print("[REMOVE] В библиотеке нет книг - удалять нечего")
        return

    to_remove = random.choice(books)
    library.remove_book(to_remove)
    print(f"[REMOVE] Удалена книга: {to_remove.get_description()}")



def event_find_by_author(library: Library) -> None:
    """
    find a book by author

    :param library: library
    :return: None
    """
    books = library.get_all_books()
    if len(books) == 0:
        print("[SEARCH] Нет книг для поиска по автору")
        return

    author = random.choice(books).author
    result = library.find_by_author(author)
    print(f"[SEARCH] Поиск по автору '{author}' → найдено {len(result)}")


def event_find_by_year(library: Library) -> None:
    """
    find a book by year

    :param library: library
    :return: None
    """
    if len(library.get_all_books()) == 0:
        print("[SEARCH] Нет книг для поиска по году")
        return

    year = random.choice(library.get_all_books()).year
    result = library.find_by_year(year)
    print(f"[SEARCH] Поиск по году {year} → найдено {len(result)}")


def event_find_existing_isbn(library: Library) -> None:
    """
    find a book by ISBN

    :param library: library
    :return: None
    """
    books = library.get_all_books()
    if len(books) == 0:
        print("[SEARCH] Нет книг для поиска по ISBN")
        return

    book = random.choice(books)
    result = library.find_by_isbn(book.isbn)
    print(f"[SEARCH] Поиск существующего ISBN {book.isbn} → найдено: {result.get_description()}")


def event_find_fake_isbn(library: Library) -> None:
    """
    try to find a book by ISBN

    :param library: library
    :return: None
    """
    fake = random.randint(10**12, 10**13 - 1)
    result = library.find_by_isbn(fake)
    if result is None:
        print(f"[SEARCH] Поиск несуществующего ISBN {fake} → книга не найдена")
    else:
        print(f"[SEARCH] Поиск существующего ISBN {result.isbn} → найдено: {result.get_description()}")

def event_get_books_count(library: Library) -> None:
    """
    get books count

    :param library: library
    :return: None
    """
    books = library.get_all_books()
    if len(books) == 0:
        print(f"[SEARCH] нет книг в библиотеке")
    else:
        print(f"[SEARCH] Сейчас в библиотеке {len(library)} книг(и)")


def run_simulator(steps: int = 20, seed: int | None = None) -> None:
    """
    run simulator to emulate the library work
    :param steps: count of steps
    :param seed: seed for random number generator
    :return: None
    """
    library = Library()

    if seed is not None:
        random.seed(seed)

    events = [
        event_add_book,
        event_remove_random_book,
        event_find_by_author,
        event_find_by_year,
        event_find_existing_isbn,
        event_find_fake_isbn,
        event_get_books_count
    ]

    for step in range(1, steps + 1):
        event = random.choice(events)
        print(f"\nШаг {step} | событие: {event.__name__}")
        try:
            event(library)
        except Exception as err:
            print(f"[ОШИБКА] {err}")
