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
