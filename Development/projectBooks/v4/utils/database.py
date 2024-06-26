from .database_connection import DatabaseConnection
from typing import List, Dict, Union

"""
Concerned with storing and retrieving books from a database 
"""

Book = Dict[str, Union[str, int]]

def create_book_table() -> None:
     with DatabaseConnection('data.db') as connection:
         cursor = connection.cursor()

         cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def add_books(name: str, author: str) -> None:
     with DatabaseConnection('data.db') as connection:
         cursor = connection.cursor()

     # cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)') This is not the recommended way because of SQL injection attack 
         cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (name, author, 0))

def get_all_books() -> List[Book]:
     with DatabaseConnection('data.db') as connection:
         cursor = connection.cursor()
         cursor.execute('SELECT * FROM books')
         books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
     return books 
          
def mark_book_as_read(name: str) -> None:
      with DatabaseConnection('data.db') as connection:
         cursor = connection.cursor()
         cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
    
def delete_book(name: str) -> None:
      with DatabaseConnection('data.db') as connection:
         cursor = connection.cursor()
         cursor.execute('DELETE from books WHERE name=?', (name,))
   


