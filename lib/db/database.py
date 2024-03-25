import sqlite3
from models.author import Author
from models.book import Book

#defune methods
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Create tables if they don't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                category INTEGER,
                year_of_publish TEXT NOT NULL,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
        ''')
        self.conn.commit()

    def create_author(self, name):
        self.cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        self.conn.commit()
        
        # Get the ID of the newly inserted author
        author_id = self.cursor.lastrowid
        
        # Fetch the author object from the database based on the ID
        self.cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        author_data = self.cursor.fetchone()
        
        # Create and return the Author object
        return Author(*author_data) if author_data else None
        
    def create_book(self, title, category, year_of_publish, copies_sold,  author_name):
        existing_author = self.find_author_by_name(author_name)
        if existing_author:
            author_id = existing_author.id
        else:
            new_author = self.create_author(author_name)
            author_id = new_author.id

        self.cursor.execute('INSERT INTO books (title, category, year_of_publish, copies_sold, author_id) VALUES (?, ?, ?, ?, ?)', 
                            (title, category, year_of_publish, copies_sold, author_id))
        self.conn.commit()
        book_id = self.cursor.lastrowid

        # Fetch only necessary fields (id, title, author_id) from the database
        self.cursor.execute('SELECT id, title, author_id FROM books WHERE id = ?', (book_id,))
        book_data = self.cursor.fetchone()

        # Fetch author details using author_id
        author = self.find_author_by_name(book_data[2])

        # Create Book object using fetched data and author object
        new_book = Book(book_data[0], book_data[1], category, year_of_publish, copies_sold, author)
        return new_book

#delete object functions
    def delete_author(self, author):
        self.authors.remove(author)

    def delete_book(self, book):
        self.books.remove(book)

    def get_all_authors(self):
        self.cursor.execute("SELECT * FROM authors")
        return self.cursor.fetchall()
   
    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def find_author_by_name(self, name):
        self.cursor.execute("SELECT * FROM authors WHERE name=?", (name,))
        author_data = self.cursor.fetchone()
        return Author(*author_data) if author_data else None

    def get_all_authors(self):
        self.cursor.execute("SELECT * FROM authors")
        authors_data = self.cursor.fetchall()
        return [Author(*author_data) for author_data in authors_data]

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

    def close(self):
        self.conn.close()

