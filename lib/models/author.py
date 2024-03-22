class Author:
    def __init__(self, id, name, books=None):
        self.id=id
        self.name = name
        self.books = books if books else[]

    def add_book(self, book):
        self.books.append(book)

    def __repr__(self):
        return f'Author(name={self.name})'
