from flask import request, Blueprint
from typing import Any, Dict, List
from src.models.genero import Genero as GeneroDoc

genero_bp = Blueprint("genero", __name__, url_prefix="/api/generos")


@genero_bp.route("", methods=["GET"])
def list_generos() -> Dict[str, Any]:
    """
    Endpoint para listar todos los géneros.

    Returns:
        Dict[str, Any]: Mensaje y lista de géneros serializados.
    """
    mensaje: str = ""
    generos_serializados: List[Dict[str, Any]] = []
    try:
        generos_doc = GeneroDoc.objects()
        for g in generos_doc:
            generos_serializados.append({
                "id": g.id if hasattr(g, "id") else None,
                "nombre": g.nombre
            })
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "generos": generos_serializados}


@genero_bp.route("", methods=["POST"])
def add_genero() -> Dict[str, Any]:
    """
    Endpoint para agregar un nuevo género.

    Returns:
        Dict[str, Any]: Estado y mensaje de la operación.
    """
    estado: bool = False
    mensaje: str = ""
    try:
        datos = request.get_json(force=True)
        genero = GeneroDoc(**datos)
        genero.save()
        estado = True
        mensaje = "Genero agregado correctamente"
    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}


@genero_bp.route("/<string:genero_id>", methods=["GET"])
def get_genero_by_id(genero_id: str) -> Dict[str, Any]:
    """
    Endpoint para obtener un género por su ID.

    Args:
        genero_id (str): ID del género.

    Returns:
        Dict[str, Any]: Mensaje y género serializado.
    """
    mensaje: str = ""
    genero_serializado: Dict[str, Any] = {}
    try:
        genero_doc = GeneroDoc.objects(id=genero_id).first()
        if not genero_doc:
            mensaje = "Género no encontrado"
        else:
            genero_serializado = {
                "id": genero_doc.id if hasattr(genero_doc, "id") else None,
                "nombre": genero_doc.nombre
            }
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "genero": genero_serializado}


@genero_bp.route("/<string:genero_id>", methods=["PUT"])
def update_genero(genero_id: str) -> Dict[str, Any]:
    """
    Endpoint para actualizar un género existente por su ID.

    Args:
        genero_id (str): ID del género.

    Returns:
        Dict[str, Any]: Estado y mensaje de la operación.
    """
    estado: bool = False
    mensaje: str = ""
    try:
        datos = request.get_json(force=True)
        genero_doc = GeneroDoc.objects(id=genero_id).first()
        if not genero_doc:
            mensaje = "Genero no encontrado para actualizar."
            return {"estado": False, "mensaje": mensaje}

        for key, value in datos.items():
            setattr(genero_doc, key, value)

        genero_doc.save()
        estado = True
        mensaje = "Genero actualizado correctamente."
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}


@genero_bp.route("/<string:genero_id>", methods=["DELETE"])
def delete_genero(genero_id: str) -> Dict[str, Any]:
    """
    Endpoint para eliminar un género por su ID.

    Args:
        genero_id (str): ID del género.

    Returns:
        Dict[str, Any]: Estado y mensaje de la operación.
    """
    estado: bool = False
    mensaje: str = ""
    try:
        genero_doc = GeneroDoc.objects(id=genero_id).first()
        if not genero_doc:
            mensaje = "Genero no encontrado para eliminar."
            return {"estado": False, "mensaje": mensaje}

        genero_doc.delete()
        estado = True
        mensaje = "Genero eliminado correctamente."

    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}
