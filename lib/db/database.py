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

    def delete_author(self, author):
        self.authors.remove(author)

    def delete_book(self, book):
        self.books.remove(book)

    def get_all_authors(self):
        return self.authors

    def get_all_books(self):
        return self.books

    def find_author_by_name(self, name):
        for author in self.authors:
            if author.name == name:
                return author
        return None

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_books_by_author(self, author_name):
        author = self.find_author_by_name(author_name)
        if author:
            return author.books
        else:
            return []

  

