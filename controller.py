from view import MovieView
from model import MovieModel
import sqlite3


class MovieController:
    def __init__(self):
        self.vista = MovieView()
        self.modelo = MovieModel()

    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                self.buscar_por_titulo()

            elif opcion == "2":
                self.buscar_por_titulo_y_anio()

            elif opcion == "3":
                self.vista.mostrar_mensaje("Hasta pronto.")
                break

            else:
                self.vista.mostrar_mensaje(
                    "Opcion incorrecta. Introduce 1, 2 o 3."
                )

    def buscar_por_titulo(self):
        titulo = self.vista.pedir_titulo()

        if titulo == "":
            self.vista.mostrar_mensaje("Debes escribir un titulo.")
            return

        respuesta = self.modelo.search_movies_by_name(titulo)

        if respuesta.get("Response") == "True":
            peliculas = respuesta.get("Search", [])
            self.vista.mostrar_peliculas(peliculas)

            if peliculas:
                self.seleccionar_pelicula(peliculas)
        else:
            self.vista.mostrar_mensaje(
                respuesta.get("Error", "No se pudo realizar la busqueda.")
            )

    def buscar_por_titulo_y_anio(self):
        titulo = self.vista.pedir_titulo()
        anio = self.vista.pedir_anio()

        if titulo == "":
            self.vista.mostrar_mensaje("Debes escribir un titulo.")
            return

        if len(anio) != 4 or not anio.isdecimal():
            self.vista.mostrar_mensaje(
                "Debes escribir un año de cuatro digitos."
            )
            return

        respuesta = self.modelo.search_movies_by_name_and_year(
            titulo, anio
        )

        if respuesta.get("Response") == "True":
            peliculas = respuesta.get("Search", [])
            self.vista.mostrar_peliculas(peliculas)
            if peliculas:
                self.seleccionar_pelicula(peliculas)
        else:
            self.vista.mostrar_mensaje(
                respuesta.get("Error", "No se pudo realizar la busqueda.")
            )

    def seleccionar_pelicula(self, peliculas):
        while True:
            seleccion = self.vista.pedir_seleccion()

            if seleccion.lower() == "salir":
                return

            try:
                numero = int(seleccion)
            except ValueError:
                self.vista.mostrar_mensaje(
                    "Introduce un numero o escribe 'salir'."
                )
                continue

            if numero < 1 or numero > len(peliculas):
                self.vista.mostrar_mensaje(
                    "Selecciona un numero de la lista."
                )
                continue

            pelicula = peliculas[numero - 1]
            detalle = self.modelo.get_movie_by_id(pelicula["imdbID"])

            if detalle.get("Response") == "True":
                self.vista.mostrar_detalle(detalle)

                try:
                    comentarios = self.modelo.get_comments_by_movie(
                        pelicula["imdbID"]
                    )
                    self.vista.mostrar_comentarios(comentarios)
                except sqlite3.Error:
                    self.vista.mostrar_mensaje(
                        "No se pudieron cargar los comentarios."
                    )

                self.agregar_comentario(pelicula["imdbID"])

            else:
                self.vista.mostrar_mensaje(
                    detalle.get("Error", "No se pudo consultar el detalle.")
                )

            return
        else:
                self.vista.mostrar_mensaje(
                    detalle.get("Error", "No se pudo consultar el detalle.")
                )

        return

    def agregar_comentario(self, imdb_id):
        opcion = self.vista.preguntar_comentario()

        if opcion != "s":
            return

        persona = self.vista.pedir_persona()
        comentario = self.vista.pedir_comentario()

        if not persona or not comentario:
            self.vista.mostrar_mensaje(
                "El nombre y el comentario no pueden estar vacios."
            )
            return

        try:
            self.modelo.add_comment(imdb_id, persona, comentario)
        except sqlite3.Error:
            self.vista.mostrar_mensaje(
                "No se pudo guardar el comentario."
            )
            return

        self.vista.mostrar_mensaje(
            "Comentario guardado correctamente."
        )

        try:
            comentarios = self.modelo.get_comments_by_movie(imdb_id)
            self.vista.mostrar_comentarios(comentarios)
        except sqlite3.Error:
            self.vista.mostrar_mensaje(
                "El comentario se guardo, pero no se pudo actualizar la lista."
            )