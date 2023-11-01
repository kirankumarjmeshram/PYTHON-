import sqlite3

connection = sqlite3.connect('bookstore')
cursor = connection.cursor()

query = '''
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
book_name TEXT,
author_name TEXT
)
'''
query1 = '''
SELECT * FROM books
'''

query2 = '''
INSERT INTO books(book_name,author_name) VALUES (?,?)
'''


cursor.execute(query2,('chetan bhagath','chetan',))

# cursor.execute(query)
connection.commit()
cursor.close()