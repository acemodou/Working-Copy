from utils import database
"""
Write a program that give us the choice to 
add a new book.
list all the books in our library 
mark a book as read 
delete a book 
q to quit 
"""

USER_CHOICE = """
- 'a' to add a new book 
- 'l' to list all books 
- 'r' to mark a book as read
- 'd' to delete a book 
- 'q' to quit

Your choice: """

        
def prompt_add_book():
    # Ask for book name and author
    book_name = input("Enter a book name: ")
    author = input("Enter the author of the book: ")
    database.add_books(book_name, author)
    
def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] =='1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_read_book():
    name = input("Enter the name of the book you just finished reading: ")

    database.mark_book_as_read(name) 

def prompt_delete_book():
    name = input("Enter the book you want to remove from your library: ")

    database.delete_book(name) 

user_options = {
    'a': prompt_add_book, 
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book
}

def menu():
    selection = input(USER_CHOICE)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print(f"Unknown input {selection}: Please enter a valid selection")
        selection = input(USER_CHOICE)

menu()
