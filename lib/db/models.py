import sqlite3

def create_database(db_name):
 
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables
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
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_name = "books.db"  
    create_database(db_name)
    print(f"SQLite database file '{db_name}' created successfully.")
