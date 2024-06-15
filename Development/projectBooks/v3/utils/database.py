import sqlite3

# """
# Concerned with storing and retrieving books from a database
# """


books_file  = 'books.db'

# def create_book_table():
#      connection = sqlite3.connect(books_file)
#      cursor = connection.cursor()

#      cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

#      connection.commit()
#      connection.close()

# def add_books(name, author):
#      connection = sqlite3.connect(books_file)
#      cursor = connection.cursor()

#      # cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)') This is not the recommended way because of SQL injection attack 
#      cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (name, author, 0))
#      connection.commit()
#      connection.close()

# def get_all_books():
#      connection = sqlite3.connect(books_file)
#      cursor = connection.cursor()
#      cursor.execute('SELECT * FROM books')
#      books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
#      connection.close()
#      return books 
          
# def mark_book_as_read(name):
#      connection = sqlite3.connect(books_file)
#      cursor = connection.cursor()
#      cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
#      connection.commit()
#      connection.close()


# def delete_book(name):
#      connection = sqlite3.connect(books_file)
#      cursor = connection.cursor()
#      cursor.execute('DELETE from books WHERE name=?', (name,))
#      connection.commit()
#      connection.close() 




def execute_query(query, parameters=(), fetch=False):
    connection = sqlite3.connect(books_file)
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    result = cursor.fetchall() if fetch else None
    connection.commit()
    connection.close()
    return result

def create_book_table():
    execute_query('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def add_books(name, author):
    execute_query('INSERT INTO books VALUES (?, ?, ?)', (name, author, 0))

def get_all_books():
    books = execute_query('SELECT * FROM books', fetch=True)
    return [{'name': row[0], 'author': row[1], 'read': row[2]} for row in books]

def mark_book_as_read(name):
    execute_query('UPDATE books SET read=1 WHERE name=?', (name,))

def delete_book(name):
    execute_query('DELETE FROM books WHERE name=?', (name,))