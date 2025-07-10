import os
from dotenv import load_dotenv  # Importa load_dotenv

load_dotenv()


class Config:
    MONGO_DBNAME = os.getenv("MONGO_DBNAME", "GestionPeliculas")
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))  # Convertir a entero

    # conexion a mongo atlas
    MONGO_URI = os.getenv("MONGO_URI")


settings = Config()
