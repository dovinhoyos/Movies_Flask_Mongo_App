from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    # The ping command is cheap and does not require auth.
    client.admin.command("ping")
    print("Conexión exitosa a MongoDB!")
except Exception as e:
    print(f"Error de conexión a MongoDB: {e}")
