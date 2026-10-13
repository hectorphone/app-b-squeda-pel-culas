from fastapi import FastAPI, HTTPException
from model import MovieModel
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import sqlite3


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"]
)

modelo = MovieModel()

class ModelComentario(BaseModel):
    persona: str = Field(min_length=1)
    comentario: str = Field(min_length=1)


@app.get("/", tags=["Home"])
def index():
    return {"mensaje": "API de peliculas funcionando"}


@app.get("/movies", tags=["Movies"])
def get_movies(titulo: str, anio: int | None = None):
    if anio is None:
        return modelo.search_movies_by_name(titulo)

    return modelo.search_movies_by_name_and_year(
        titulo, str(anio)
    )

@app.get("/movies/{imdb_id}", tags=["Movies"])
def get_movie_detail(imdb_id: str):
    return modelo.get_movie_by_id(imdb_id)


@app.get("/movies/{imdb_id}/comentarios", tags=["Comentarios"])
def get_comments(imdb_id: str):
    try:
        return modelo.get_comments_by_movie(imdb_id)
    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="No se pudieron cargar los comentarios."
        )

@app.post("/movies/{imdb_id}/comentarios", tags=["Comentarios"])
def create_comment(imdb_id: str, body: ModelComentario):
    persona = body.persona.strip()
    comentario = body.comentario.strip()

    if not persona or not comentario:
        raise HTTPException(
            status_code=400,
            detail="El nombre y el comentario no pueden estar vacios."
        )

    try:
        id_comentario = modelo.add_comment(
            imdb_id, persona, comentario
        )
    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="No se pudo guardar el comentario."
        )

    return {
        "mensaje": "Comentario guardado correctamente.",
        "id": id_comentario
    }