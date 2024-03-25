import sqlite3
from models.author import Author
from models.book import Book

#defune methods
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Creates tables if they don't exist
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
        
        # Getting the ID of the newly inserted author
        author_id = self.cursor.lastrowid
        
        # Fetching the author object from the database based on the ID
        self.cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        author_data = self.cursor.fetchone()
        
        # Creating and return the Author object
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

        self.cursor.execute('SELECT id, title, author_id FROM books WHERE id = ?', (book_id,))
        book_data = self.cursor.fetchone()

        author = self.find_author_by_name(book_data[2])

        new_book = Book(book_data[0], book_data[1], category, year_of_publish, copies_sold, author)
        return new_book

    def delete_book(self, book_id):
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        books_data = self.cursor.fetchall()
        return [Book(*book_data) for book_data in books_data]
        
    def get_books_by_author(self, author_name):
        self.cursor.execute("SELECT * FROM books WHERE author_id IN (SELECT id FROM authors WHERE name = ?)", (author_name,))
        books_data = self.cursor.fetchall()
        return [Book(*book_data) for book_data in books_data]

    def get_books_by_year(self, year):
        self.cursor.execute("SELECT * FROM books WHERE year_of_publish = ?", (year,))
        books_data = self.cursor.fetchall()
        return [Book(*book_data) for book_data in books_data]

    def get_books_by_category(self, category):
        self.cursor.execute("SELECT * FROM books WHERE category = ?", (category,))
        books_data = self.cursor.fetchall()
        return [Book(*book_data) for book_data in books_data]
    
    def find_author_by_id(self, author_id):
        self.cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        author_data = self.cursor.fetchone()
        return Author(*author_data) if author_data else None

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
        
    def find_author_by_id(self, author_id):
        self.cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        author_data = self.cursor.fetchone()
        return Author(*author_data) if author_data else None

    def get_book_by_id(self, book_id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book_data = self.cursor.fetchone()
        if book_data:
            author = self.find_author_by_id(book_data[4])  # Fetch author using author_id
            return Book(*book_data[:-1], author)
        else:
            return None
        
    def update_book(self, book_id, title=None, category=None, year_of_publish=None, copies_sold=None, author_name=None):
        # Checking if the book with the given ID exists
        book = self.find_book_by_id(book_id)
        if not book:
            print("Book not found.")
            return None

        # Updating the details of the book
        if title is not None:
            book.title = title
        if category is not None:
            book.category = category
        if year_of_publish is not None:
            book.year_of_publish = year_of_publish
        if copies_sold is not None:
            book.copies_sold = copies_sold
        if author_name is not None:
            # Checking if the author exists or create a new one
            author = self.find_author_by_name(author_name)
            if not author:
                author = self.create_author(author_name)
            # Updating the book's author ID
            book.author_id = author.id

        # Updating the book in the database
        self.cursor.execute('UPDATE books SET title=?, category=?, year_of_publish=?, copies_sold=?, author_id=? WHERE id=?',
                            (book.title, book.category, book.year_of_publish, book.copies_sold, book.author_id, book_id))
        self.conn.commit()

        return book

    def close(self):
        self.conn.close()

