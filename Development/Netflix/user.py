from netflix import Movie 


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []
    
    def __repr__(self):
        return f"<User {self.name}>"
    
    def add_movie(self, name, genre):
        movie = Movie(name, genre, False) 
        self.movies.append(movie)
    
    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # already_watch = []
        # for movie in self.movies:
        #     if movie.watched:
        #         already_watch.append(movie)
        # return already_watch
        return list(filter(lambda movie: movie.watched, self.movies))
    
    def save_to_file(self):
        with open(f'{self.name}.txt', 'w') as f:
            f.write(self.name +"\n")
            for movie in self.movies:
                f.write(f"{movie.name},{movie.genre},{movie.watched} \n")
    
    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
        username = content[0]
        view_contents = []
        for lines in content[1:]:
            info = lines.split(",")
            view_contents.append(Movie(info[0], info[1], str(info[2])==""))
        user_account = cls(username)
        user_account.movies = view_contents
        return user_account
    
    def json(self):
        return {
            'name':self.name,
            'movies':[
                movie.json() for movie in self.movies
            ]
        }
    
    @classmethod
    def from_json(cls, json_data):
        user_name = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user_name.movies = movies
        return user_name 


        

