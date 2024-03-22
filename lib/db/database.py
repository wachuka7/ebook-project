from models.book import Book
from models.author import Author

class Database:
    def __init__(self):
        self.authors = []
        self.books = []

    def create_author(self, name):
        author = Author(name)
        self.authors.append(author)
        return author

    def create_book(self, title, author):
        book = Book(title, author)
        author.add_book(book)
        self.books.append(book)
        return book

 
