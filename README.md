# 🎬 Movies_Flask_Mongo_App

API simple para gestionar películas y géneros usando Flask y MongoDB.

---

## 🛠️ Tecnologías

- ⚡ Flask
- 🍃 MongoDB + MongoEngine

## 🚀 Instalación

1. 🧑‍💻 Cloná el repo y entrá a la carpeta:
   ```bash
   git clone <repo-url>
   cd Movies_Flask_Mongo_App
   ```
2. 📦 Instalá dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. ⚙️ Configurá tu `.env`:
   ```
   MONGO_DBNAME=GestionPeliculas
   MONGO_URI=mongodb://localhost:27017/GestionPeliculas
   ```
4. ▶️ Levantá el servidor:
   ```bash
   python3 app.py
   ```

## Estructura

```
Movies_Flask_Mongo_App/
│
├── app.py                # Archivo principal, inicia la app y registra rutas
│
├── src/
│   ├── models/           # Modelos de datos (MongoEngine)
│   │   ├── pelicula.py   # Modelo Pelicula
│   │   └── genero.py     # Modelo Genero
│   │
│   ├── routes/           # Endpoints REST
│   │   ├── peliculas.py  # Rutas de películas
│   │   └── generos.py    # Rutas de géneros
│   │
│   ├── domain/           # Entidades limpias (lógica de negocio)
│   │   ├── pelicula.py
│   │   └── genero.py
│   │
│   ├── adapters/         # Adaptadores (transforman datos entre capas)
│   │   ├── pelicula_adapter.py
│   │   └── genero_adapter.py
│   │
│   ├── database/         # Inicialización y conexión a la base de datos
│   │   └── mongo.py
│   │
│   └── config.py         # Configuración y variables de entorno
│
├── requirements.txt      # Dependencias del proyecto
├── .env                  # Variables de entorno (no incluido en el repo)
└── README.md             # Documentación
```

## 📚 Endpoints principales

### 🎬 Películas
- `GET /api/peliculas` — Lista todas las películas.
- `POST /api/peliculas` — Crea una película.
- `GET /api/peliculas/<id>` — Trae una película por id.
- `PUT /api/peliculas/<id>` — Actualiza una película.
- `DELETE /api/peliculas/<id>` — Elimina una película.

### 🎭 Géneros
- `GET /api/generos` — Lista todos los géneros.
- `POST /api/generos` — Crea un género.
- `GET /api/generos/<id>` — Trae un género por id.
- `PUT /api/generos/<id>` — Actualiza un género.
- `DELETE /api/generos/<id>` — Elimina un género.

## ⚡ Ejemplo rápido con curl

```bash
# 🎭 Crear género
curl -X POST http://localhost:5000/api/generos -H "Content-Type: application/json" -d '{"nombre": "Comedia"}'

# 🎬 Crear película
curl -X POST http://localhost:5000/api/peliculas -H "Content-Type: application/json" -d '{"codigo": 101, "titulo": "Risas", "protagonista": "Ana", "duracion": 90, "resumen": "Comedia divertida", "foto": "risas.jpg", "genero": "<ID_DEL_GENERO>"}'

# 📋 Listar películas
curl http://localhost:5000/api/peliculas
```

## Notas

- Usá los IDs que vienen en las respuestas para relacionar géneros y películas.
- La estructura permite escalar, testear y migrar fácil.
- Configurá tu base y variables de entorno antes de levantar el server.
