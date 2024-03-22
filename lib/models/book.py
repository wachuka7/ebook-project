class Book:
    def __init__(self, id, title, author):
        self.id=id
        self.title = title
        self.author = author

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author})'
