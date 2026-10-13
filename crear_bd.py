import sqlite3


conexion = sqlite3.connect("moviesearch.db")

try:
    with open("create_tables.sql", "r", encoding="utf-8") as archivo:
        sql = archivo.read()

    conexion.executescript(sql)
    conexion.commit()

    print("Base de datos y tabla comentario creadas correctamente.")
finally:
    conexion.close()