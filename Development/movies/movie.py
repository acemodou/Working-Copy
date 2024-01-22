class Movies:
    def __init__(self) -> None:
        self.movies = []
    def __len__(self):
        return len(self.movies)




movie = Movies()
movie.movies.append("The Matrix")
movie.movies.append("The Titanic")

print(len(movie))