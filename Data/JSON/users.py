from movie import Movie 

class User:
    def __init__(self, name):
        self.name = name 
        self.movies = []
    
    def __repr__(self):
        return "<Login>:{}".format(self.name)
    
    def add_movies(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)
    
    def delete_movie(self, name):
        '''
        Iterate through self.movies and if the name doesn't match
        Filter it out. 
        Need to learn more what lambda does. 
        '''
        self.movies = list(filter(lambda movie:movie.name != name, self.movies))
            
    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True 
    
    def watched_movies(self):
        watched_movies_list = []
        for movie in self.movies:
            if movie.watched:
                watched_movies_list.append(movie)
        return watched_movies_list
    
    def JSON(self):
        return{
            'name':self.name,
            'movies':[
                movie.json() for movie in self.movies
            ]
        }
    
    @classmethod
    def user_json(cls, json_data):
        user = json_data['name']

        movies = []
        for film in json_data['movies']:
            movies.append(Movie.from_json(film))
        user.movies = movies
        return user 

