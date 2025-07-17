from typing import Optional
from src.models.pelicula import Pelicula as PeliculaDoc
from src.models.genero import Genero as GeneroDoc
from src.domain.pelicula import Pelicula as PeliculaDomain
from src.domain.genero import Genero as GeneroDomain


def mongo_to_domain_genero(genero_doc: Optional[GeneroDoc]) -> Optional[GeneroDomain]:
    """
    Convierte un documento Genero de MongoEngine a una entidad de dominio Genero.

    Args:
        genero_doc (Optional[GeneroDoc]): Documento Genero de MongoEngine.

    Returns:
        Optional[GeneroDomain]: Entidad de dominio Genero.
    """
    if genero_doc is None:
        return None
    return GeneroDomain(nombre=genero_doc.nombre, id=str(genero_doc.id))


def mongo_to_domain_pelicula(pelicula_doc: Optional[PeliculaDoc]) -> Optional[PeliculaDomain]:
    """
    Convierte un documento Pelicula de MongoEngine a una entidad de dominio Pelicula.
    Incluye el id real del documento.

    Args:
        pelicula_doc (Optional[PeliculaDoc]): Documento Pelicula de MongoEngine.

    Returns:
        Optional[PeliculaDomain]: Entidad de dominio Pelicula.
    """
    if pelicula_doc is None:
        return None
    genero_domain = mongo_to_domain_genero(pelicula_doc.genero)
    pelicula_domain = PeliculaDomain(
        codigo=pelicula_doc.codigo,
        titulo=pelicula_doc.titulo,
        protagonista=pelicula_doc.protagonista,
        duracion=pelicula_doc.duracion,
        resumen=pelicula_doc.resumen,
        foto=getattr(pelicula_doc, "foto", None),
        genero=genero_domain
    )
    # Agregar el id real como atributo extra
    setattr(pelicula_domain, "id", str(pelicula_doc.id))
    return pelicula_domain


def domain_to_mongo_genero(genero_domain: Optional[GeneroDomain]) -> Optional[GeneroDoc]:
    """
    Convierte una entidad de dominio Genero a un documento Genero de MongoEngine.

    Args:
        genero_domain (Optional[GeneroDomain]): Entidad de dominio Genero.

    Returns:
        Optional[GeneroDoc]: Documento Genero de MongoEngine.
    """
    if genero_domain is None:
        return None
    genero_doc = GeneroDoc.objects(nombre=genero_domain.nombre).first()
    if genero_doc is None:
        genero_doc = GeneroDoc(nombre=genero_domain.nombre)
        genero_doc.save()
    return genero_doc


def domain_to_mongo_pelicula(pelicula_domain: Optional[PeliculaDomain]) -> Optional[PeliculaDoc]:
    """
    Convierte una entidad de dominio Pelicula a un documento Pelicula de MongoEngine.

    Args:
        pelicula_domain (Optional[PeliculaDomain]): Entidad de dominio Pelicula.

    Returns:
        Optional[PeliculaDoc]: Documento Pelicula de MongoEngine.
    """
    if pelicula_domain is None:
        return None
    genero_doc = domain_to_mongo_genero(pelicula_domain.genero)
    pelicula_doc = PeliculaDoc(
        codigo=pelicula_domain.codigo,
        titulo=pelicula_domain.titulo,
        protagonista=pelicula_domain.protagonista,
        duracion=pelicula_domain.duracion,
        resumen=pelicula_domain.resumen,
        foto=pelicula_domain.foto,
        genero=genero_doc
    )
    return pelicula_doc
