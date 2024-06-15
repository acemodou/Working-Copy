"""
Concerned with storing and retrieving books from a list
"""

books = []
def add_books(name, author):
     books.append({
        "name": name, 
        'author': author, 
        'read': False
    })

def get_books():
     return books

def mark_book_as_read(name):
     for book in books:
          if book['name'] == name:
               book['read'] = True 

# def delete_book(name):
#      # Its a bad practice to remove items from a list whilst iterating over them
#      # This works but is certainly a bad practice 
#      for book in books:
#           if book['name'] == name:
#                books.remove(book)

def delete_book(name):
     # add each book to new list if book['name'] != name
     global books 
     books = [book for book in books if book['name'] != name]