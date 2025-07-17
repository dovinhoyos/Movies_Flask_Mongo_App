from typing import Any
from flask import Flask
from flask_mongoengine import MongoEngine
from src.config import settings

db: MongoEngine = MongoEngine()

def init_db(app: Flask) -> None:
    """
    Inicializa la base de datos MongoEngine con la configuración de la app Flask.

    Args:
        app (Flask): Instancia de la aplicación Flask.
    """
    app.config["MONGODB_SETTINGS"] = [
        {
            "db": settings.MONGO_DBNAME,
            "host": settings.MONGO_URI
        }
    ]
    db.init_app(app)
