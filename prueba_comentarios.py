from consultas import insertar_comentario, comentarios_por_pelicula


id_comentario = insertar_comentario(
    "tt0133093",
    "Hector",
    "Comentario de prueba para Matrix"
)

print("Comentario creado:", id_comentario)
print(comentarios_por_pelicula("tt0133093"))