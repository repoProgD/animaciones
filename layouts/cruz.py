from manim import *

def cruz(base_objeto, direccion='vertical', cantidad=5, espacio=1.0):
    """
    Crea un layout vertical u horizontal basado en un objeto base. Luego, crea copias a lo largo de la dirección seleccionada.

    Parámetros:
    - base_objeto: El objeto que se va a copiar
    - direccion: 'vertical' o 'horizontal'
    - cantidad: Número de copias a crear
    - espacio: Distancia entre las copias

    Retorna:
    - Un grupo con los objetos copiados.
    """
    copias = []
    for i in range(cantidad):
        copia = base_objeto.copy()

        if direccion == 'vertical':
            copia.move_to(UP * (i * espacio))  # Mueve la copia verticalmente
        elif direccion == 'horizontal':
            copia.move_to(RIGHT * (i * espacio))  # Mueve la copia horizontalmente

        copias.append(copia)

    return Group(*copias)
