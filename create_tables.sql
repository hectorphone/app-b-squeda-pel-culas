CREATE TABLE IF NOT EXISTS comentario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pelicula TEXT NOT NULL,
    persona TEXT NOT NULL,
    comentario TEXT NOT NULL,
    fecha TEXT NOT NULL
);