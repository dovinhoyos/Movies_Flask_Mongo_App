from app import app
from flask import request
from models.genero import Genero


@app.route("/genero/", methods=["GET"])
def listGeneros():
    """
    _summary_
    Función que retorna la lista de generos
    existentes en la colección generos

    Returns:
        _type_: lista de generos
    """
    try:
        mensaje = None
        generos = Genero.objects()
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "generos": generos}


@app.route("/genero/", methods=["POST"])
def addGenero():
    try:
        mensaje = None
        estado = False
        if request.method == "POST":
            datos = request.get_json(force=True)
            genero = Genero(**datos)
            genero.save()
            estado = True
            mensaje = "Genero agregado correctamente"
        else:
            mensaje = "No permitido"
    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}


@app.route("/genero/<string:genero_id>", methods=["GET"])
def getGeneroById(genero_id):
    """
    Función que retorna un genero específico por su ID.
    """
    try:
        mensaje = None
        genero = Genero.objects(id=genero_id).first()
        if not genero:
            mensaje = "Género no encontrado"
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "genero": genero}


@app.route("/genero/<string:genero_id>", methods=["PUT"])
def updateGenero(genero_id):
    """
    Función que actualiza un género existente por su ID.
    """
    try:
        mensaje = None
        estado = False
        if request.method == "PUT":
            datos = request.get_json(force=True)

            genero = Genero.objects(id=genero_id).first()
            if not genero:
                mensaje = "Genero no encontrado para actualizar."
                return {"estado": False, "mensaje": mensaje}

            # Actualizar solo los campos proporcionados en el JSON
            for key, value in datos.items():
                setattr(genero, key, value)  # setattr(object, name, value)

            genero.save()  # Guardar los cambios
            estado = True
            mensaje = "Genero actualizado correctamente."
        else:
            mensaje = "Metodo no permitido."
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}


@app.route("/genero/<string:genero_id>", methods=["DELETE"])
def deleteGenero(genero_id):
    """
    Función que elimina un género por su ID.
    """
    try:
        mensaje = None
        estado = False

        genero = Genero.objects(id=genero_id).first()
        if not genero:
            mensaje = "Genero no encontrado para eliminar."
            return {"estado": False, "mensaje": mensaje}

        # Opcional: Podrías añadir una validación aquí
        # para evitar eliminar un género que está referenciado por películas.
        # Si lo eliminas, el campo 'genero' en las películas que lo referencian
        # quedará 'roto' o nulo, dependiendo de cómo lo maneje MongoEngine/MongoDB.
        # Para esta implementación sencilla, simplemente lo eliminamos.

        genero.delete()  # Eliminar el documento
        estado = True
        mensaje = "Genero eliminado correctamente."

    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}
