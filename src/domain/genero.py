"""
Dominio: Entidad Genero

Representa el género de una película en la capa de dominio.
No depende de frameworks ni de la base de datos.
"""

from typing import Optional


class Genero:
    """
    Entidad de dominio para Género.
    """

    def __init__(self, nombre: str, id: Optional[str] = None) -> None:
        """
        Inicializa un género.

        Args:
            nombre (str): Nombre del género.
            id (Optional[str]): Identificador único del género (opcional).
        """
        self.id = id
        self.nombre = nombre

    def __repr__(self) -> str:
        return f"Genero(id={self.id}, nombre='{self.nombre}')"
