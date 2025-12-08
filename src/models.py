class LibraryItem:
    """
    Base class for library items
    """
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self) -> str:
        """Return description of the item(book)"""
        return f"{self.title} - {self.author}, {self.year}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.title}, {self.author}, {self.year}"


class Book(LibraryItem):
    """Default book"""
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: int):
        super().__init__(title, author, year)
        self.genre = genre
        self.isbn = isbn

    def get_description(self) -> str:
        """Return description of the book"""
        return f"Книга: {self.title} - {self.author}, {self.year}, жанр: {self.genre}"


class RareBook(Book):
    """Rare book"""
    def __init__(self, title: str, author: str, year: int, genre: str,
                 isbn: int, price: int, rarity_level: int = 5):
        super().__init__(title, author, year, genre, isbn)
        self.price = price
        self.rarity_level = rarity_level

    def get_description(self) -> str:
        """Return description of the rare book"""
        return (f"[RARE] {self.title} - {self.author}, {self.year}, "
                f"жанр: {self.genre}, цена: {self.price}₽, "
                f"уровень редкости: {self.rarity_level}/10")


class DigitalBook(Book):
    """Digital book"""
    def __init__(self, title: str, author: str, year: int,
                 genre: str, isbn: int, file_format: str = "PDF", pages: int = 0):
        super().__init__(title, author, year, genre, isbn)
        self.file_format = file_format
        self.pages = pages

    def get_description(self) -> str:
        """Return description of the digital book"""
        return (f"[E-BOOK] {self.title} - {self.author}, {self.year}, жанр: {self.genre}, "
                f"формат: {self.file_format}, страниц: {self.pages}")
