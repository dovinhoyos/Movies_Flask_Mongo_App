from app import app
from flask import request
from models.pelicula import Pelicula
from models.genero import Genero


@app.route("/pelicula/", methods=["GET"])
def listPelicula():
    try:
        mensaje = None
        peliculas = Pelicula.objects()
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "peliculas": peliculas}


@app.route("/pelicula/", methods=["POST"])
def addPelicula():
    try:
        mensaje = None
        estado = False
        if request.method == "POST":
            datos = request.get_json(force=True)

            genero_id = datos.get(
                "genero"
            )  # Obtener el ID del género del JSON de entrada

            if not genero_id:
                mensaje = "El campo 'genero' es requerido."
                return {"estado": False, "mensaje": mensaje}

            # Buscar si el género existe en la base de datos
            genero_existente = Genero.objects(id=genero_id).first()

            if not genero_existente:
                mensaje = f"El género con ID '{genero_id}' no existe."
                return {"estado": False, "mensaje": mensaje}

            # Si el género existe, asignarlo al campo 'genero' de los datos para la película
            datos["genero"] = genero_existente

            pelicula = Pelicula(**datos)
            pelicula.save()
            estado = True
            mensaje = "Pelicula agregada correctamente"
        else:
            mensaje = "No permitido"
    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}


@app.route("/pelicula/<string:pelicula_id>", methods=["GET"])
def getPeliculaById(pelicula_id):
    """
    Función que retorna una película específica por su ID.
    """
    try:
        mensaje = None
        pelicula = Pelicula.objects(id=pelicula_id).first()
        if not pelicula:
            mensaje = "Pelicula no encontrada"
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "pelicula": pelicula}


@app.route("/pelicula/<string:pelicula_id>", methods=["PUT"])
def updatePelicula(pelicula_id):
    """
    Función que actualiza una película existente por su ID.
    """
    try:
        mensaje = None
        estado = False
        if request.method == "PUT":
            datos = request.get_json(force=True)

            pelicula = Pelicula.objects(id=pelicula_id).first()
            if not pelicula:
                mensaje = "Pelicula no encontrada para actualizar."
                return {"estado": False, "mensaje": mensaje}

            # Validar y actualizar el campo 'genero' si está presente en los datos
            if "genero" in datos:
                genero_id = datos.get("genero")
                if not genero_id:
                    mensaje = "El ID de genero no puede estar vacío."
                    return {"estado": False, "mensaje": mensaje}

                genero_existente = Genero.objects(id=genero_id).first()
                if not genero_existente:
                    mensaje = f"El genero con ID '{genero_id}' no existe para la actualizacion."
                    return {"estado": False, "mensaje": mensaje}
                datos["genero"] = genero_existente  # Asignar el objeto Genero

            # Actualizar el resto de los campos proporcionados
            for key, value in datos.items():
                # Evitar actualizar el ID de la película (aunque MongoEngine lo manejaría)
                if key != "id":
                    setattr(pelicula, key, value)

            pelicula.save()
            estado = True
            mensaje = "Pelicula actualizada correctamente."
        else:
            mensaje = "Método no permitido."
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}


@app.route("/pelicula/<string:pelicula_id>", methods=["DELETE"])
def deletePelicula(pelicula_id):
    try:
        mensaje = None
        estado = False

        pelicula = Pelicula.objects(id=pelicula_id).first()
        if not pelicula:
            mensaje = "Pelicula no encontrada para eliminar."
            return {"estado": False, "mensaje": mensaje}

        pelicula.delete()  # Eliminar el documento
        estado = True
        mensaje = "Pelicula eliminada correctamente."

    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}
