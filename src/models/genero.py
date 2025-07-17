from mongoengine import Document, StringField
from typing import Optional

class Genero(Document):
    """
    Modelo de persistencia para Género.
    Hereda de MongoEngine Document y representa la colección 'generos' en la base de datos.

    Attributes:
        nombre (str): Nombre del género.
    """
    nombre: StringField = StringField(max_length=50, unique=True, required=True)

    @property
    def id(self) -> Optional[str]:
        """
        Retorna el identificador único del género como string.

        Returns:
            Optional[str]: El id del género.
        """
        return str(self.pk) if self.pk else None

    def __repr__(self) -> str:
        return f"Genero(id={self.id}, nombre='{self.nombre}')"
