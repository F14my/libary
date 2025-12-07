class Book:
    """The book model"""
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: int):
        """Initialize the book model"""
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self):
        return f"""
        Title: {self.title}
        Author: {self.author}
        Year: {self.year}
        Genre: {self.genre}
        ISBN: {self.isbn}
        """