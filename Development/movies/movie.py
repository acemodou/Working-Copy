Movies = []

def add_movies():
    name = input("Enter your movie name: ")
    title = input("Enter your movie title: ")
    releaseYear = int(input("Enter the year the movie was release: "))
    Movies.append({
        'name': name, 
        'title':title.title(),
        'year': releaseYear
    })

def show_movies():
    for movie in Movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Name: {movie['name']},\n Title: {movie['title']} ,\n Release Year : {movie['year']}")

def find_movies():
    search_title = input("What movie are you looking for: ")
    for movie in Movies:
        if movie['title'] == search_title:
            print_movie(movie)
        else:
            print(f"{search_title} you are looking for not in collection")
