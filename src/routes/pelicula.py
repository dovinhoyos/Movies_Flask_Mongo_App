from flask import request, Blueprint
from typing import Any, Dict
from src.models.pelicula import Pelicula as PeliculaDoc
from src.models.genero import Genero as GeneroDoc
from src.adapters.pelicula_adapter import mongo_to_domain_pelicula
from src.domain.pelicula import Pelicula as PeliculaDomain

pelicula_bp = Blueprint("pelicula", __name__, url_prefix="/api/peliculas")


@pelicula_bp.route("", methods=["GET"])
def list_peliculas() -> Dict[str, Any]:
    """
    Endpoint para listar todas las películas.
    Utiliza el adaptador para devolver entidades limpias y serializadas.

    Returns:
        Dict[str, Any]: Mensaje y lista de películas serializadas.
    """
    mensaje: str = ""
    peliculas_serializadas: list = []
    try:
        peliculas_doc = PeliculaDoc.objects()
        peliculas_domain = [mongo_to_domain_pelicula(p) for p in peliculas_doc]
        for p in peliculas_domain:
            genero_obj = None
            if p.genero:
                genero_obj = {
                    "id": p.genero.id,
                    "nombre": p.genero.nombre
                }
            peliculas_serializadas.append({
                "id": p.id if hasattr(p, "id") else None,
                "codigo": p.codigo,
                "titulo": p.titulo,
                "protagonista": p.protagonista,
                "duracion": p.duracion,
                "resumen": p.resumen,
                "foto": p.foto,
                "genero": genero_obj
            })
    except Exception as error:
        mensaje = str(error)
    return {"mensaje": mensaje, "peliculas": peliculas_serializadas}


@pelicula_bp.route("", methods=["POST"])
def add_pelicula() -> Dict[str, Any]:
    """
    Endpoint para agregar una nueva película.
    Utiliza el adaptador y entidades limpias.

    Returns:
        Dict[str, Any]: Estado y mensaje de la operación.
    """
    estado: bool = False
    mensaje: str = ""
    try:
        datos = request.get_json(force=True)
        genero_id = datos.get("genero")
        if not genero_id:
            mensaje = "El campo 'genero' es requerido."
            return {"estado": False, "mensaje": mensaje}

        genero_existente = GeneroDoc.objects(id=genero_id).first()
        if not genero_existente:
            mensaje = f"El género con ID '{genero_id}' no existe."
            return {"estado": False, "mensaje": mensaje}

        pelicula_domain = PeliculaDomain(
            codigo=datos.get("codigo"),
            titulo=datos.get("titulo"),
            protagonista=datos.get("protagonista"),
            duracion=datos.get("duracion"),
            resumen=datos.get("resumen"),
            foto=datos.get("foto"),
            genero=mongo_to_domain_pelicula(PeliculaDoc(genero=genero_existente)).genero
        )
        pelicula_doc = PeliculaDoc(
            codigo=pelicula_domain.codigo,
            titulo=pelicula_domain.titulo,
            protagonista=pelicula_domain.protagonista,
            duracion=pelicula_domain.duracion,
            resumen=pelicula_domain.resumen,
            foto=pelicula_domain.foto,
            genero=genero_existente
        )
        pelicula_doc.save()
        estado = True
        mensaje = "Pelicula agregada correctamente"
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}


@pelicula_bp.route("/<string:pelicula_id>", methods=["GET"])
def get_pelicula_by_id(pelicula_id: str) -> Dict[str, Any]:
    """
    Endpoint para obtener una película por su ID.

    Args:
        pelicula_id (str): ID de la película.

    Returns:
        Dict[str, Any]: Mensaje y película serializada.
    """
    mensaje: str = ""
    pelicula_serializada: Dict[str, Any] = {}
    try:
        pelicula_doc = PeliculaDoc.objects(id=pelicula_id).first()
        pelicula_domain = mongo_to_domain_pelicula(pelicula_doc)
        if not pelicula_domain:
            mensaje = "Pelicula no encontrada"
        else:
            genero_obj = None
            if pelicula_domain.genero:
                genero_obj = {
                    "id": pelicula_domain.genero.id,
                    "nombre": pelicula_domain.genero.nombre
                }
            pelicula_serializada = {
                "id": pelicula_domain.id if hasattr(pelicula_domain, "id") else None,
                "codigo": pelicula_domain.codigo,
                "titulo": pelicula_domain.titulo,
                "protagonista": pelicula_domain.protagonista,
                "duracion": pelicula_domain.duracion,
                "resumen": pelicula_domain.resumen,
                "foto": pelicula_domain.foto,
                "genero": genero_obj
            }
    except Exception as error:
        mensaje = str(error)
    return {"mensaje": mensaje, "pelicula": pelicula_serializada}


@pelicula_bp.route("/<string:pelicula_id>", methods=["PUT"])
def update_pelicula(pelicula_id: str) -> Dict[str, Any]:
    """
    Endpoint para actualizar una película existente por su ID.

    Args:
        pelicula_id (str): ID de la película.

    Returns:
        Dict[str, Any]: Estado y mensaje de la operación.
    """
    estado: bool = False
    mensaje: str = ""
    try:
        datos = request.get_json(force=True)
        pelicula_doc = PeliculaDoc.objects(id=pelicula_id).first()
        if not pelicula_doc:
            mensaje = "Pelicula no encontrada para actualizar."
            return {"estado": False, "mensaje": mensaje}

        # Validar y actualizar el campo 'genero' si está presente en los datos
        if "genero" in datos:
            genero_id = datos.get("genero")
            if not genero_id:
                mensaje = "El ID de genero no puede estar vacío."
                return {"estado": False, "mensaje": mensaje}
            genero_existente = GeneroDoc.objects(id=genero_id).first()
            if not genero_existente:
                mensaje = f"El genero con ID '{genero_id}' no existe para la actualizacion."
                return {"estado": False, "mensaje": mensaje}
            datos["genero"] = genero_existente  # Asignar el objeto Genero

        # Actualizar el resto de los campos proporcionados
        for key, value in datos.items():
            if key != "id":
                setattr(pelicula_doc, key, value)

        pelicula_doc.save()
        estado = True
        mensaje = "Pelicula actualizada correctamente."
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}


@pelicula_bp.route("/<string:pelicula_id>", methods=["DELETE"])
def delete_pelicula(pelicula_id: str) -> Dict[str, Any]:
    """
    Endpoint para eliminar una película por su ID.

    Args:
        pelicula_id (str): ID de la película.

    Returns:
        Dict[str, Any]: Estado y mensaje de la operación.
    """
    estado: bool = False
    mensaje: str = ""
    try:
        pelicula_doc = PeliculaDoc.objects(id=pelicula_id).first()
        if not pelicula_doc:
            mensaje = "Pelicula no encontrada para eliminar."
            return {"estado": False, "mensaje": mensaje}

        pelicula_doc.delete()
        estado = True
        mensaje = "Pelicula eliminada correctamente."
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}
