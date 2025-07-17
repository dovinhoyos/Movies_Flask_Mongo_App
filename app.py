from flask import Flask
from src.database.db import init_db
from src.routes.pelicula import pelicula_bp
from src.routes.genero import genero_bp


def create_app():
    """
    Crea una instancia de la aplicación Flask y configura el entorno.
    """
    app = Flask(__name__)

    app.config["UPLOAD_FOLDER"] = "./static/imagenes"
    init_db(app)

    app.register_blueprint(pelicula_bp)
    app.register_blueprint(genero_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, host="0.0.0.0", debug=True)
