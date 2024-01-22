MENU_PROMPT = "\n Enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie by title or 'q' to quit:"

movies = []
def add_movies():
    title = input("Enter title: ")
    director = input("Enter director: ")
    year = int(input("Enter year: "))
    movies.append(
        {'title' : title,
         'director' : director,
         'year' : year}
    )


def list_movies():
    for movie in movies:
        print_movie(movie)


def find_movie():
    search_movie = input("Enter movie title you are looking for: ")
    for movie in movies:
        if movie["title"] == search_movie:
            print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

user_options = {
    "a" : add_movies,
    "l" : list_movies,
    "f" : find_movie
}

def menu():
    selection = input("Enter your selection: ")
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
          
        else:
            print("Unknown command. Please try again.")
        selection = input(MENU_PROMPT)
    

menu()
        