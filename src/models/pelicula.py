from mongoengine import Document, StringField, IntField, ReferenceField
from src.models.genero import Genero
from typing import Optional

class Pelicula(Document):
    """
    Modelo de persistencia para la colección Pelicula en MongoDB.

    Atributos:
        codigo (int): Código único de la película.
        titulo (str): Título de la película.
        protagonista (str): Nombre del protagonista.
        duracion (int): Duración en minutos.
        resumen (str): Breve descripción.
        foto (str): URL de la imagen.
        genero (Genero): Referencia al género.
    """
    codigo: int = IntField(unique=True, required=True)
    titulo: str = StringField(max_length=80, required=True)
    protagonista: str = StringField(max_length=50, required=True)
    duracion: int = IntField(min_value=30, max_value=200, required=True)
    resumen: str = StringField(required=True)
    foto: Optional[str] = StringField()
    genero: Optional[Genero] = ReferenceField(Genero)

    @property
    def id(self) -> str:
        """Devuelve el id único de la película como string."""
        return str(self.pk)

    def __repr__(self) -> str:
        return f"Pelicula(id={self.id}, titulo='{self.titulo}')"
