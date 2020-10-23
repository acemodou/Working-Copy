import os 
import json
from users import User
from movie import Movie


_DATAPATH = os.path.dirname(os.path.realpath(__file__)) 

def menu():
    '''
    Check if file exist for the user
    If it already exists, welcome them and load their data
    If not create a user object
    '''
    name = input("Enter your login name: ")
    filename = "{}.txt".format(name)
    path = os.path.join(_DATAPATH, filename)
    print("{}! Netflix is storing your login info at {}".format(name, path))
    if file_exist(path):
        print("Welcome to Netflix {}".format(name))
        with open(path, 'r') as f:
            json_data = json.load(f)
        user = User.user_json(json_data)
    else:
        user = User(name)
        print("Welcome back! {}".format(user))

        #TODO: Give them a list of options 
        #TODO: Add a movie 
        #TODO: See list of movies 
        #TODO: Set a movie as watched 
        #TODO: Delete a movie by name 
        #TODO: See list of watched movies 
        #TODO: Save and quit
        user_input = input("Enter 'a' to add a movie, 'p' to see the list of movies,"
                       "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                       ", 'f' to save or 'q' to quit: ")
        
        while user_input != 'q':
            if user_input == 'a':
                movie_name = input("Enter the movie name: ")
                movie_genre = input("Enter the movie genre: ")
                user.add_movies(movie_name, movie_genre)
            elif user_input == 'p':
                for movie in user.movies:
                    print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
            elif user_input == 'w':
                movie_name = input("Enter the movie name to set as watched: ")
                user.set_watched(movie_name)
            elif user_input == 'd':
                movie_name = input("Enter the movie name to delete: ")
                user.delete_movie(movie_name)
            elif user_input == 'l':
                for movie in user.watched_movies():
                    print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
            elif user_input == 's':
                with open(filename, 'w') as f:
                    json.dump(user.JSON(), f)

            
            user_input = input("Enter 'a' to add a movie, 'p' to see the list of movies,"
                       "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                       ", 's' to save or 'q' to quit: ")
        
            
def file_exist(path):
    return os.path.isfile(path)


menu()


