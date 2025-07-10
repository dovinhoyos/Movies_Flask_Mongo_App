from config import settings
from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_db(app):
    app.config["MONGODB_SETTINGS"] = [
        {"db": settings.MONGO_DBNAME, "host": settings.MONGO_URI}
    ]

    db.init_app(app)
