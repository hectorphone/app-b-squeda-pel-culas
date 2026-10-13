import sqlite3


class Conexion:
    def __init__(self, sql_query, parametros=()):
        self.con = sqlite3.connect("moviesearch.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

        try:
            self.res = self.cur.execute(sql_query, parametros)
        except sqlite3.Error:
            self.con.close()
            raise