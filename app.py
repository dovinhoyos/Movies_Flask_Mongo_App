from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv  # Importa load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "./static/imagenes"

MONGO_DBNAME = os.getenv("MONGO_DBNAME", "GestionPeliculas")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))  # Convertir a entero

# coneccion a mongo atlas
MONGO_URI = os.getenv("MONGO_URI")

app.config["MONGODB_SETTINGS"] = [{"db": MONGO_DBNAME, "host": MONGO_URI}]

db = MongoEngine(app)

if __name__ == "__main__":
    from routes.genero import *
    from routes.pelicula import *

    app.run(port=5000, host="0.0.0.0", debug=True)
