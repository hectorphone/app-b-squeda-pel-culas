const formulario = document.getElementById("formBuscar");
const mensaje = document.getElementById("mensaje");


function buscarPeliculas(evento) {
    evento.preventDefault();

    const titulo = document.getElementById("titulo").value.trim();

    if (titulo === "") {
        mensaje.textContent = "Escribe un titulo para buscar.";
        return;
    }

    mensaje.textContent = `Has escrito: ${titulo}`;
}


formulario.addEventListener("submit", buscarPeliculas);