const parametros = new URLSearchParams(window.location.search);
const imdbId = parametros.get("imdb_id");

const mensaje = document.getElementById("mensaje");


function cargarDetalle() {
    if (!imdbId) {
        mensaje.textContent = "Falta el identificador de la pelicula.";
        return;
    }

    mensaje.textContent = "Cargando pelicula...";

    fetch(`http://127.0.0.1:8000/movies/${encodeURIComponent(imdbId)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            return response.json();
        })
        .then(pelicula => {
            if (pelicula.Response === "False") {
                mensaje.textContent = pelicula.Error;
                return;
            }

            // Colocamos los datos de la pelicula en la pagina
            document.getElementById("titulo").textContent = pelicula.Title;
            document.getElementById("anio").textContent = pelicula.Year;
            document.getElementById("director").textContent = pelicula.Director;
            document.getElementById("actores").textContent = pelicula.Actors;
            document.getElementById("sinopsis").textContent = pelicula.Plot;

            const cartel = document.getElementById("cartel");

            if (pelicula.Poster && pelicula.Poster !== "N/A") {
                cartel.src = pelicula.Poster;
                cartel.alt = `Cartel de ${pelicula.Title}`;
                cartel.hidden = false;
            }

            document.getElementById("detalle").hidden = false;
            mensaje.textContent = "";
            cargarComentarios();
        })
        .catch(error => {
            mensaje.textContent = "No se pudo cargar la pelicula.";
            console.log("Error al cargar el detalle:", error);
        });
}
function cargarComentarios() {
    const mensajeComentarios = document.getElementById("mensajeComentarios");
    const comentarios = document.getElementById("comentarios");

    document.getElementById("seccionComentarios").hidden = false;
    comentarios.textContent = "";
    mensajeComentarios.textContent = "Cargando comentarios...";

    fetch(`http://127.0.0.1:8000/movies/${encodeURIComponent(imdbId)}/comentarios`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            if (data.length === 0) {
                mensajeComentarios.textContent = "Todavia no hay comentarios.";
                return;
            }

            mensajeComentarios.textContent = "";

            // Mostramos quien lo ha escrito, la fecha y el comentario
            data.forEach(comentario => {
                const bloque = document.createElement("div");
                bloque.className = "border rounded p-3 mb-3";

                const persona = document.createElement("p");
                persona.className = "fw-bold";
                persona.textContent = `${comentario.persona} (${comentario.fecha})`;

                const texto = document.createElement("p");
                texto.textContent = comentario.comentario;

                bloque.appendChild(persona);
                bloque.appendChild(texto);
                comentarios.appendChild(bloque);
            });
        })
        .catch(error => {
            mensajeComentarios.textContent = "No se pudieron cargar los comentarios.";
            console.log("Error al cargar los comentarios:", error);
        });
}

cargarDetalle();