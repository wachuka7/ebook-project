import sqlite3

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Creating tables
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
            category_id INTEGER,
            year_of_publish INTEGER,
            copies_sold INTEGER,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def add_data(db_name, authors_data, books_data, categories_data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for author_name in authors_data:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))

    for category_name in categories_data:
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))

    for book_info in books_data:
        title, category_name, year_of_publish, copies_sold, author_id = book_info
        cursor.execute("SELECT id FROM categories WHERE name=?", (category_name,))
        category_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO books (title, category_id, year_of_publish, copies_sold, author_id) VALUES (?, ?, ?, ?, ?)",
                       (title, category_id, year_of_publish, copies_sold, author_id,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_name = "books.db"  
    create_database(db_name)
    print(f"SQLite database file '{db_name}' created successfully.")

    authors_data = ["Rachael", "Mike", "Joe", "Frank"]  # List of authors
    categories_data = ["Finances", "Technology", "Health", "Fashion"]  # List of categories
    books_data = [
        ("Finance and Wealth", "Finances", 2020, 100, 4),  
        ("AI Today", "Technology", 2019, 150, 3),
        ("Morning Diet", "Health", 2021, 80, 2),
        ("Trending Wigs", "Fashion", 2021, 570, 1),
        ("Finance and Wealth", "Finances", 2023, 124, 2),  
        ("Best Sellers Today", "Fashion", 2012, 340, 1),
        ("Exercises for all Body Types", "Health", 2024, 30, 3),
        ("Latest Shoes", "Fashion", 2020, 230, 1),
    ]  

    add_data(db_name, authors_data, books_data, categories_data)
    print("Data added successfully.")
