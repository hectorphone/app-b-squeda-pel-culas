from model import MovieModel


modelo = MovieModel()
respuesta = modelo.search_movies_by_name("matrix")

print(respuesta)