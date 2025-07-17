from typing import Optional
from .genero import Genero

class Pelicula:
    """
    Entidad de dominio para representar una película en el sistema.

    Esta clase no depende de frameworks ni de la base de datos.
    Sirve para encapsular la lógica de negocio y las propiedades
    principales de una película.
    """

    def __init__(
        self,
        codigo: int,
        titulo: str,
        protagonista: str,
        duracion: int,
        resumen: str,
        foto: Optional[str],
        genero: Optional[Genero]
    ):
        self.codigo: int = codigo
        self.titulo: str = titulo
        self.protagonista: str = protagonista
        self.duracion: int = duracion
        self.resumen: str = resumen
        self.foto: Optional[str] = foto
        self.genero: Optional[Genero] = genero

    def __repr__(self) -> str:
        return f"Pelicula(codigo={self.codigo}, titulo='{self.titulo}')"
