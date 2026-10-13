from conexion import Conexion
from datetime import date


def formato(respuesta):
    lista_final = []

    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))

    return lista_final


def comentarios_por_pelicula(id_pelicula):
    conexion = Conexion(
        "SELECT * FROM comentario WHERE id_pelicula = ? ORDER BY id;",
        (id_pelicula,)
    )

    try:
        return formato(conexion.res)
    finally:
        conexion.con.close()


def insertar_comentario(id_pelicula, persona, comentario):
    fecha = date.today().isoformat()

    conexion = Conexion(
        """
        INSERT INTO comentario
        (id_pelicula, persona, comentario, fecha)
        VALUES (?, ?, ?, ?);
        """,
        (id_pelicula, persona, comentario, fecha)
    )

    try:
        conexion.con.commit()
        return conexion.cur.lastrowid
    finally:
        conexion.con.close()