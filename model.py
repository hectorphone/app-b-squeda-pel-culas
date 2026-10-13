import requests as consulta
from consultas import comentarios_por_pelicula
from config import API_KEY
from consultas import comentarios_por_pelicula, insertar_comentario


class MovieModel:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://www.omdbapi.com/"

    def search_movies_by_name(self, nombre: str):
        try:
            respuesta = consulta.get(
                self.base_url,
                params={
                    "s": nombre,
                    "apikey": self.api_key,
                    "type": "movie"
                },
                timeout=10
            )

            respuesta.raise_for_status()
            return respuesta.json()

        except consulta.RequestException:
            return {
                "Response": "False",
                "Error": "No se pudo conectar con OMDb."
            }
    def search_movies_by_name_and_year(self, nombre: str, anio: str):
        try:
            respuesta = consulta.get(
                self.base_url,
                params={
                    "s": nombre,
                    "y": anio,
                    "apikey": self.api_key,
                    "type": "movie"
                },
                timeout=10
            )

            respuesta.raise_for_status()
            return respuesta.json()

        except consulta.RequestException:
            return {
                "Response": "False",
                "Error": "No se pudo conectar con OMDb."
            }
    def get_movie_by_id(self, imdb_id: str):
        try:
            respuesta = consulta.get(
                self.base_url,
                params={
                    "i": imdb_id,
                    "plot": "full",
                    "apikey": self.api_key
                },
                timeout=10
            )

            respuesta.raise_for_status()
            return respuesta.json()

        except consulta.RequestException:
            return {
                "Response": "False",
                "Error": "No se pudo conectar con OMDb."
            }
    def get_comments_by_movie(self, imdb_id: str):
        return comentarios_por_pelicula(imdb_id)

    def add_comment(self, imdb_id: str, persona: str, comentario: str):
        return insertar_comentario(imdb_id, persona, comentario)