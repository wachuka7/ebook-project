import sqlite3

CONN = sqlite3.connect('book.db')
CURSOR = CONN.cursor()
