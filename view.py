class MovieView:
    def mostrar_menu(self):
        print("\n====================================")
        print("  BUSCADOR DE PELICULAS EN OMDB")
        print("====================================")
        print("1 - Buscar pelicula por titulo")
        print("2 - Buscar pelicula por titulo y año")
        print("3 - Salir")

        return input("\nSelecciona una opcion: ").strip()

    def pedir_titulo(self):
        return input("\nIntroduce el nombre de la pelicula: ").strip()

    def mostrar_peliculas(self, peliculas):
        print("\n====================================")
        print("  RESULTADOS DE LA BUSQUEDA")
        print("====================================")

        for numero, pelicula in enumerate(peliculas, start=1):
            print(
                f"{numero} - {pelicula['Title']} "
                f"({pelicula['Year']}) [{pelicula['Type']}]"
            )

    def mostrar_mensaje(self, mensaje):
        print(f"\n{mensaje}")

    def pedir_anio(self):
        return input("Introduce el año de la pelicula: ").strip()

    def pedir_seleccion(self):
        return input(
            "\nSelecciona el numero de la pelicula "
            "(o escribe 'salir' para volver al menu): "
        ).strip()

    def mostrar_detalle(self, pelicula):
        print("\n====================================")
        print("  INFORMACION DE LA PELICULA")
        print("====================================")

        print("Titulo:", pelicula.get("Title", "No disponible"))
        print("Año:", pelicula.get("Year", "No disponible"))
        print("Director:", pelicula.get("Director", "No disponible"))
        print("Actores:", pelicula.get("Actors", "No disponible"))
        print("Genero:", pelicula.get("Genre", "No disponible"))
        print("Duracion:", pelicula.get("Runtime", "No disponible"))
        print("Sinopsis:", pelicula.get("Plot", "No disponible"))

    def mostrar_comentarios(self, comentarios):
        print("\n====================================")
        print("  COMENTARIOS DE LA PELICULA")
        print("====================================")

        if not comentarios:
            print("Todavia no hay comentarios.")
            return

        for comentario in comentarios:
            print(
                f"\n{comentario['persona']} "
                f"({comentario['fecha']})"
            )
            print(comentario["comentario"])

    def preguntar_comentario(self):
        return input(
            "\n¿Quieres añadir un comentario? (s/n): "
        ).strip().lower()

    def pedir_persona(self):
        return input("Introduce tu nombre: ").strip()

    def pedir_comentario(self):
        return input("Escribe tu comentario: ").strip()