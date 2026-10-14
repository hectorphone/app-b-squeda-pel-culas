const url = "http://127.0.0.1:8000/movies";

const formulario = document.getElementById("formBuscar");
const mensaje = document.getElementById("mensaje");
const resultados = document.getElementById("resultados");


function buscarPeliculas(evento) {
    evento.preventDefault();

    const titulo = document.getElementById("titulo").value.trim();
    const anio = document.getElementById("anio").value;

    resultados.textContent = "";

    if (titulo === "") {
        mensaje.textContent = "Escribe un titulo para buscar.";
        return;
    }

    // Preparamos el titulo y, si lo has escrito, el año
    const parametros = new URLSearchParams();
    parametros.set("titulo", titulo);

    if (anio !== "") {
        parametros.set("anio", anio);
    }

    mensaje.textContent = "Buscando peliculas...";

    fetch(`${url}?${parametros.toString()}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            if (data.Response === "False") {
                mensaje.textContent = data.Error;
                return;
            }

            mensaje.textContent = "";

            // Mostramos el titulo y el año de cada pelicula
            data.Search.forEach(pelicula => {
                const columna = document.createElement("div");
                columna.className = "col-12 col-md-6 col-lg-4 mb-4";

                const tarjeta = document.createElement("div");
                tarjeta.className = "card h-100";

                // Añadimos el cartel si la pelicula tiene uno
                if (pelicula.Poster && pelicula.Poster !== "N/A") {
                    const imagen = document.createElement("img");
                    imagen.src = pelicula.Poster;
                    imagen.alt = `Cartel de ${pelicula.Title}`;
                    imagen.className = "card-img-top";
                    imagen.style.height = "350px";
                    imagen.style.objectFit = "contain";

                    tarjeta.appendChild(imagen);
                }

                const cuerpo = document.createElement("div");
                cuerpo.className = "card-body";

                const titulo = document.createElement("h2");
                titulo.className = "card-title h5";
                titulo.textContent = pelicula.Title;

                const anio = document.createElement("p");
                anio.className = "card-text";
                anio.textContent = `Año: ${pelicula.Year}`;

                cuerpo.appendChild(titulo);
                cuerpo.appendChild(anio);
                                // Pasamos el identificador a la pagina de detalle
                const enlace = document.createElement("a");
                enlace.className = "btn btn-primary";
                enlace.textContent = "Ver detalle";
                enlace.href = `detalle.html?imdb_id=${encodeURIComponent(pelicula.imdbID)}`;
                cuerpo.appendChild(enlace);
                tarjeta.appendChild(cuerpo);
                columna.appendChild(tarjeta);
                resultados.appendChild(columna);
            });
        })
        .catch(error => {
            mensaje.textContent = "No se pudo realizar la busqueda.";
            console.log("Error al buscar peliculas:", error);
        });
}


formulario.addEventListener("submit", buscarPeliculas);