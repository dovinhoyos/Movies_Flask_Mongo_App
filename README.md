# Movies_Flask_Mongo_App

¡Bienvenido/a a Movies_Flask_Mongo_App! 🎬

Esta aplicación es una API RESTful desarrollada con Flask y MongoDB (usando MongoEngine) pensada para la gestión integral de películas y géneros. Permite realizar operaciones CRUD (crear, leer, actualizar y eliminar) tanto para películas como para géneros, de manera fácil y rápida.

Ideal como base para proyectos educativos, pruebas de conceptos o como backend para aplicaciones de catálogo de películas.

---

## 🛠️ Tecnologías principales

- **Flask**: Framework web minimalista de Python para construir APIs de manera rápida y flexible.
- **MongoDB**: Base de datos NoSQL ideal para almacenar documentos JSON (en este caso, películas y géneros).
- **MongoEngine**: ODM (Object Document Mapper) para trabajar con MongoDB usando objetos Python.
- **Flask-MongoEngine**: Integración sencilla entre Flask y MongoEngine.
- **python-dotenv**: Permite manejar variables de entorno de forma segura, ideal para guardar datos sensibles como URIs y credenciales.

Extras:

- Soporte tanto para MongoDB local como para Atlas.
- Estructura lista para escalar y agregar autenticación.

---

## 🚀 Instalación y configuración

### Requisitos previos

- Python 3.8+
- pip
- Una instancia de MongoDB (local o MongoDB Atlas)

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/Movies_Flask_Mongo_App.git
cd Movies_Flask_Mongo_App
```

### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 3. Configura las variables de entorno

Crea un archivo `.env` en la raíz del proyecto con los siguientes datos:

```env
MONGO_DBNAME=GestionPeliculas
MONGO_URI=mongodb+srv://<usuario>:<password>@<tu-cluster>.mongodb.net/GestionPeliculas?retryWrites=true&w=majority
# Para local usa algo como:
# MONGO_URI=mongodb://localhost:27017/GestionPeliculas
```

Asegurate de tener tu base corriendo y accesible.

### 4. Ejecuta la aplicación

```bash
python app.py
```

Por defecto corre en `http://localhost:5000`

---

## 📁 Estructura del proyecto

```plaintext
Movies_Flask_Mongo_App/
├── app.py               # Entrada principal de la app Flask
├── config.py            # Configuración y lectura de variables de entorno
├── requirements.txt     # Dependencias
├── models/              # Modelos de MongoDB (Pelicula, Genero)
├── routes/              # Rutas (pelicula.py, genero.py)
├── database/            # Inicialización y conexión con MongoDB
└── ...                  # Otros archivos utilitarios
```

- **app.py**: Punto de entrada y registro de rutas.
- **models/**: Define los modelos de datos con MongoEngine.
- **routes/**: Define los endpoints de la API REST.
- **database/**: Lógica de conexión/creación de la base de datos.
- **config.py**: Maneja variables de entorno y configuración.

Esta estructura permite escalar fácil y separar responsabilidades de manera limpia.

---

## 📚 Endpoints disponibles

### Películas

- **GET /api/peliculas**  
  Devuelve todas las películas.

  **Response ejemplo:**

  ```json
  {
    "mensaje": null,
    "peliculas": [ ... ]
  }
  ```

- **POST /api/peliculas**  
  Crea una nueva película. El body debe incluir:

  ```json
  {
    "codigo": 123,
    "titulo": "Matrix",
    "protagonista": "Keanu Reeves",
    "duracion": 120,
    "resumen": "Película de acción y ciencia ficción.",
    "foto": "matrix.jpg",
    "genero": "<ID del género>"
  }
  ```

  **Response ejemplo:**

  ```json
  {
    "estado": true,
    "mensaje": "Pelicula agregada correctamente"
  }
  ```

- **GET /api/peliculas/<pelicula_id>**  
  Devuelve una película por su ID.

  **Response ejemplo:**

  ```json
  {
    "mensaje": null,
    "pelicula": { ... }
  }
  ```

- **PUT /api/peliculas/<pelicula_id>**  
  Actualiza los campos de una película existente.

  **Request ejemplo:**

  ```json
  {
    "titulo": "Matrix Reloaded",
    "genero": "<ID de género nuevo>"
  }
  ```

  **Response ejemplo:**

  ```json
  {
    "estado": true,
    "mensaje": "Pelicula actualizada correctamente."
  }
  ```

- **DELETE /api/peliculas/<pelicula_id>**  
  Elimina una película por su ID.

  **Response ejemplo:**

  ```json
  {
    "estado": true,
    "mensaje": "Pelicula eliminada correctamente."
  }
  ```

### Géneros

- **GET /api/generos**  
  Devuelve todos los géneros.

  **Response ejemplo:**

  ```json
  {
    "mensaje": null,
    "generos": [ ... ]
  }
  ```

- **POST /api/generos**  
  Crea un nuevo género. El body debe incluir:

  ```json
  {
    "nombre": "Ciencia Ficción"
  }
  ```

  **Response ejemplo:**

  ```json
  {
    "estado": true,
    "mensaje": "Genero agregado correctamente"
  }
  ```

- **GET /api/generos/<genero_id>**  
  Devuelve un género por su ID.

  **Response ejemplo:**

  ```json
  {
    "mensaje": null,
    "genero": { ... }
  }
  ```

- **PUT /api/generos/<genero_id>**  
  Actualiza campos de un género existente.

  **Request ejemplo:**

  ```json
  {
    "nombre": "Acción"
  }
  ```

  **Response ejemplo:**

  ```json
  {
    "estado": true,
    "mensaje": "Genero actualizado correctamente."
  }
  ```

- **DELETE /api/generos/<genero_id>**  
  Elimina un género por su ID.

  **Response ejemplo:**

  ```json
  {
    "estado": true,
    "mensaje": "Genero eliminado correctamente."
  }
  ```

---

## 🧪 Ejemplos de uso con curl

### Crear un género

```bash
curl -X POST http://localhost:5000/api/generos \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Comedia"}'
```

### Listar géneros

```bash
curl http://localhost:5000/api/generos
```

### Crear una película

```bash
curl -X POST http://localhost:5000/api/peliculas \
     -H "Content-Type: application/json" \
     -d '{
           "codigo": 101,
           "titulo": "Inception",
           "protagonista": "Leonardo DiCaprio",
           "duracion": 148,
           "resumen": "Un ladrón que roba secretos a través de sueños.",
           "foto": "inception.jpg",
           "genero": "<ID_DEL_GENERO>"
         }'
```

### Listar películas

```bash
curl http://localhost:5000/api/peliculas
```

### Actualizar una película

```bash
curl -X PUT http://localhost:5000/api/peliculas/<ID_DE_PELICULA> \
     -H "Content-Type: application/json" \
     -d '{ "titulo": "Inception (2010)" }'
```

### Eliminar un género

```bash
curl -X DELETE http://localhost:5000/api/generos/<ID_DEL_GENERO>
```

### Eliminar una película

```bash
curl -X DELETE http://localhost:5000/api/peliculas/<ID_DE_PELICULA>
```

---

## 📝 Notas y recomendaciones de desarrollo

- La estructura del proyecto facilita agregar autenticación, middlewares o tests sin romper nada.
- Si necesitas extender modelos, usá siempre los tipos de datos de MongoEngine y validaciones propias.
- Las rutas están desacopladas de los modelos, así que podés migrar a FastAPI o Django Rest sin dramas.
- Usá variables de entorno para no hardcodear URIs ni credenciales.
- Los IDs de películas y géneros son de MongoDB (ObjectId). Usá los IDs tal como vienen en los responses.
- Para PRs o cambios, mantené el formato de las respuestas para no romper frontend o integraciones.
- Si querés hacer deploy en Heroku, Railway o Render, sólo tenés que ajustar la variable MONGO_URI y listo.

---

## 🙌 Créditos y licencia

Creado por Richard Parker!

Licencia MIT. ¡Usalo, compartilo y mejoralo!
