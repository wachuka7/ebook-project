class Book:
    def __init__(self, id, title, category, year_of_publish, copies_sold, author_id):
        self.id=id
        self.title = title
        self.category=category
        self.year_of_publish=year_of_publish
        self.copies_sold=copies_sold
        self.author_id = author_id

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author})'
