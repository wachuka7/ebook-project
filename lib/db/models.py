import sqlite3

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            category TEXT,
            publish_year INTEGER,
            total_sold INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    ''')

    conn.commit()
    conn.close()

def add_data(db_name, authors_data, books_data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for author_name in authors_data:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))

    for book_info in books_data:
        title, author_id, category, publish_year, total_sold = book_info
        cursor.execute("INSERT INTO books (title, author_id, category, publish_year, total_sold) VALUES (?, ?, ?, ?, ?)",
                       (title, author_id, category, publish_year, total_sold))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_name = "books.db"  
    create_database(db_name)
    print(f"SQLite database file '{db_name}' created successfully.")

    authors_data = ["Rachael", "Mike", "Joe", "Frank"]  # List of authors
    books_data = [
        ("Finance and Wealth", 4, "Finances", 2020, 100),  
        ("AI Today", 3, "Technology", 2019, 150),
        ("Morning Diet", 2, "Health", 2021, 80),
        ("Trending Wigs", 1, "Fashion", 2021, 570),
        ("Finance and Wealth", 2, "Finances", 2023, 124),  
        ("Best Sellers Today", 1, "Fashion", 2012, 340),
        ("Exercises for all Body Types", 7, "Health", 2024, 30),
        ("Latest Shoes", 1, "Fashion", 2020, 230),
    ]  

    add_data(db_name, authors_data, books_data)
    print("Data added successfully.")
