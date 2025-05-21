from manim import *


def en_grilla(grupo: VGroup, columnas: int, espacio_x: float = 1.0, espacio_y: float = 1.0,
              alineacion_horizontal: str = "centro", alineacion_vertical: str = "centro",
              max_izquierda: float = -6, max_derecha: float = 6,
              max_abajo: float = -3.5, max_arriba: float = 3.5,
              offset_x: float = 0, offset_y: float = 0) -> VGroup:
    """
    Distribuye un grupo de objetos en una grilla, organizados en filas y columnas,
    dentro de límites definidos, con espacio entre objetos y opciones de alineación.

    Parámetros:
    - grupo: VGroup con los objetos a distribuir
    - columnas: cantidad de columnas deseadas
    - espacio_x: espacio horizontal entre objetos
    - espacio_y: espacio vertical entre objetos
    - alineacion_horizontal: 'izquierda', 'centro' o 'derecha'
    - alineacion_vertical: 'arriba', 'centro' o 'abajo'
    - max_izquierda / max_derecha: límites horizontales
    - max_abajo / max_arriba: límites verticales
    - offset_x / offset_y: corrimientos adicionales

    Retorna:
    - El mismo grupo, con objetos reposicionados
    """
    n = len(grupo)
    filas = (n + columnas - 1) // columnas

    # Posicionar los objetos en forma de grilla
    for idx, obj in enumerate(grupo):
        fila = idx // columnas
        col = idx % columnas
        obj.move_to([col * espacio_x, -fila * espacio_y, 0])

    # Calculamos el ancho y alto de la grilla
    ancho_total = (min(columnas, n) - 1) * espacio_x
    alto_total = (filas - 1) * espacio_y

    # Alineación horizontal
    if alineacion_horizontal == "centro":
        grupo.shift(RIGHT * ((max_derecha + max_izquierda - ancho_total) / 2 + offset_x))
    elif alineacion_horizontal == "izquierda":
        grupo.shift(LEFT * abs(max_izquierda) + RIGHT * offset_x)
    elif alineacion_horizontal == "derecha":
        grupo.shift(RIGHT * abs(max_derecha - ancho_total) + RIGHT * offset_x)

    # Alineación vertical
    if alineacion_vertical == "centro":
        grupo.shift(UP * ((max_arriba + max_abajo - alto_total) / 2 + offset_y))
    elif alineacion_vertical == "arriba":
        grupo.shift(UP * abs(max_arriba) + UP * offset_y)
    elif alineacion_vertical == "abajo":
        grupo.shift(DOWN * abs(max_abajo - alto_total) + UP * offset_y)

    return grupo

