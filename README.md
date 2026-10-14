# Proyecto final Bootcamp Aprender a programar desde cero XXVI


Este es mi proyecto final del Bootcamp Aprender a Programar desde Cero XXVI de KeepCoding.

La aplicación permite buscar películas por título o por título y año, consultar su información y guardar comentarios en SQLite. Los datos de las películas vienen de [OMDb](https://www.omdbapi.com/).

Empecé haciendo una versión de consola para entender la lógica y después añadí FastAPI y las pantallas web. Las dos versiones utilizan el mismo modelo y la misma base de datos.

## Qué funciona por ahora

- Búsqueda por título y por título más año, en consola y en la web.
- Resultados con cartel, título y año en la web.
- Consulta del detalle de una película en consola, API y web.
- Registro y lectura de comentarios desde la consola, la API y la web.
- Guardado de comentarios con nombre, identificador de película y fecha actual.
- Validación para evitar nombres y comentarios vacíos o formados solo por espacios.

La página de detalle ya muestra los comentarios guardados y permite añadir uno nuevo. Al guardarlo, la lista se actualiza y el formulario se limpia. La puntuación de 1 a 5 y el promedio en estrellas son una funcionalidad opcional que todavía no está implementada.

El año se utiliza como filtro adicional al título, según la aclaración del profesor. No se realiza una búsqueda únicamente por año.

## Tecnologías

Python, Requests, FastAPI, Pydantic, Uvicorn, SQLite, HTML, JavaScript y Bootstrap.

He trabajado con Python 3.14 en Windows y VS Code. Las versiones de las librerías están en `requirements.txt`. SQLite viene incluido en Python.

## Preparar el proyecto

Los siguientes comandos son para PowerShell en Windows. Hay que ejecutarlos desde la carpeta principal del proyecto.

### 1. Descargar el repositorio

```powershell
git clone https://github.com/hectorphone/app-b-squeda-pel-culas.git
cd app-b-squeda-pel-culas
```

También se puede descargar el ZIP desde GitHub, descomprimirlo y abrir la carpeta en VS Code.

### 2. Crear el entorno e instalar las librerías

```powershell
py -m venv entorno
.\entorno\Scripts\python.exe -m pip install -r requirements.txt
```

Los comandos utilizan directamente el Python del entorno, así que no hace falta activarlo para ejecutarlos.

### 3. Configurar la clave de OMDb

Solicita una clave en [OMDb](https://www.omdbapi.com/apikey.aspx) y actívala desde el enlace del correo recibido.

Crea un archivo llamado `config.py` junto a `model.py` y escribe tu clave entre comillas:

```python
API_KEY = "TU_CLAVE_DE_OMDB"
```

Este archivo está excluido en `.gitignore` y no se sube al repositorio. Cada persona que descargue el proyecto debe crear el suyo.

Se necesita conexión a Internet para consultar OMDb y cargar Bootstrap y los carteles.

### 4. Crear la base de datos

```powershell
.\entorno\Scripts\python.exe crear_bd.py
```

Este comando crea `moviesearch.db` y la tabla `comentario` a partir de `create_tables.sql`. Si ya existen, conserva los datos.

El repositorio incluye una base de datos con comentarios de prueba. El script de creación no los borra.

El identificador de película se guarda como texto para conservar el IMDb ID completo, por ejemplo `tt0133093`.

## Ejecutar la aplicación web

Necesitamos dos terminales abiertas en la carpeta principal.

En la primera, arrancamos la API:

```powershell
.\entorno\Scripts\python.exe -m uvicorn controller_api:app --reload
```

En la segunda, arrancamos la página web:

```powershell
.\entorno\Scripts\python.exe -m http.server 5500 --directory frontend
```

Abre el [buscador](http://127.0.0.1:5500/), escribe un título, añade el año si quieres y pulsa **Buscar**. El botón **Ver detalle** abre la información de la película seleccionada.

Debajo del detalle puedes leer los comentarios y escribir el tuyo indicando tu nombre. Pulsa **Guardar comentario** y espera la confirmación. No se permiten campos vacíos ni formados solo por espacios.

La [documentación de FastAPI](http://127.0.0.1:8000/docs) permite probar las rutas de la API.

Mantén las dos terminales abiertas mientras utilizas la web. Para detener cada servidor, pulsa `Ctrl+C` en su terminal. La configuración CORS permite el frontend en `http://127.0.0.1:5500`.

## Ejecutar la versión de consola

```powershell
.\entorno\Scripts\python.exe main.py
```

El menú permite buscar por título o por título y año. Después puedes seleccionar una película por su número, ver el detalle, leer sus comentarios y añadir uno nuevo. Escribe `salir` para volver desde la selección o elige la opción `3` para cerrar el programa.

## Rutas de la API

| Método | Ruta | Qué hace |
| --- | --- | --- |
| GET | `/` | Comprueba que la API está funcionando. |
| GET | `/movies?titulo=matrix&anio=1999` | Busca películas; el año es opcional. |
| GET | `/movies/{imdb_id}` | Consulta el detalle por identificador. |
| GET | `/movies/{imdb_id}/comentarios` | Recupera los comentarios de esa película. |
| POST | `/movies/{imdb_id}/comentarios` | Guarda un comentario. |

Para probar el POST en `/docs`, introduce `tt0133093` en `imdb_id` y un cuerpo como este:

```json
{
  "persona": "Hector",
  "comentario": "Me encanta esta pelicula"
}
```

Cada envío crea un comentario nuevo. La fecha se añade automáticamente.

## Cómo he organizado el código

- `main.py`: arranca la consola.
- `controller.py`: coordina el menú, las búsquedas y los comentarios.
- `view.py`: muestra la información y pide los datos en la consola.
- `model.py`: consulta OMDb y accede a los comentarios.
- `controller_api.py`: recibe las peticiones de FastAPI y utiliza el mismo modelo.
- `conexion.py`: contiene la clase de conexión con SQLite.
- `consultas.py`: guarda y recupera los comentarios.
- `crear_bd.py` y `create_tables.sql`: crean la base de datos y la tabla.
- `frontend/index.html` y `frontend/js/app.js`: formulario y resultados de búsqueda.
- `frontend/detalle.html` y `frontend/js/detalle.js`: información de la película seleccionada.
- `requirements.txt`: dependencias con sus versiones.

La organización sigue el patrón MVC: el modelo trabaja con los datos, la vista los presenta y el controlador conecta las acciones del usuario con el modelo.

## Comprobaciones realizadas

Se han probado búsquedas por título y año, selección y detalle en consola, registro y lectura de comentarios, persistencia después de reiniciar y rechazo de comentarios con nombre vacío. También se han probado las rutas de la API, la búsqueda web con y sin año, la lectura y el guardado de comentarios desde la web y el rechazo de un nombre formado solo por espacios sin crear otro registro.

`prueba_model.py` consulta OMDb. `prueba_comentarios.py` inserta un comentario de prueba en la base de datos del proyecto cada vez que se ejecuta.
