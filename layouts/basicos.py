from manim import *

def en_linea_horizontal(grupo: VGroup, espacio: float = 1.0, alineacion: str = "centro", 
                         max_izquierda: float = -5, max_derecha: float = 5, altura: float = 0) -> VGroup:
    """
    Distribuye un grupo de objetos en línea horizontal con espacio uniforme dentro de límites,
    considerando el tamaño total de los objetos, de manera que cuanto mayor sea el grupo,
    menos se puede desplazar hacia los bordes. También permite mover el grupo verticalmente
    según el parámetro altura.

    Parámetros:
    - grupo: VGroup con los objetos a distribuir
    - espacio: distancia horizontal entre objetos
    - alineacion: 'centro', 'izquierda' o 'derecha'
    - max_izquierda: límite izquierdo del área de distribución
    - max_derecha: límite derecho del área de distribución
    - altura: valor para mover el grupo en el eje Y (positivo para arriba, negativo para abajo)

    Retorna:
    - El mismo grupo, con objetos reposicionados
    """
    n = len(grupo)

    # Calcular el ancho total que ocuparán los objetos (considerando el espacio entre ellos)
    ancho_total_objetos = sum([objeto.width for objeto in grupo]) + (n - 1) * espacio

    # Calcular un factor de desplazamiento que sea inversamente proporcional al ancho total del grupo
    factor_desplazamiento = max(0.5, (max_derecha - max_izquierda) / ancho_total_objetos)

    # Calcular la distancia máxima que puede moverse el grupo hacia la izquierda o la derecha
    desplazamiento_max_izquierda = (max_izquierda + ancho_total_objetos / 2) * factor_desplazamiento
    desplazamiento_max_derecha = (max_derecha - ancho_total_objetos / 2) * factor_desplazamiento

    # Colocar los objetos en una línea horizontal con el espacio especificado
    for i, obj in enumerate(grupo):
        obj.move_to([i * espacio, 0, 0])

    # Alineación según el parámetro horizontal
    if alineacion == "centro":
        # Mover al grupo al centro dentro de los límites
        desplazamiento = (desplazamiento_max_derecha - desplazamiento_max_izquierda - ancho_total_objetos) / 2
        grupo.shift(RIGHT * (desplazamiento + desplazamiento_max_izquierda))

    elif alineacion == "izquierda":
        # Mover al grupo a la izquierda, dentro de los límites
        grupo.shift(LEFT * desplazamiento_max_izquierda)

    elif alineacion == "derecha":
        # Mover al grupo a la derecha, dentro de los límites
        grupo.shift(RIGHT * desplazamiento_max_derecha)

    # Mover el grupo verticalmente según el parámetro altura
    grupo.shift(UP * altura)

    return grupo


def en_linea_vertical(grupo: VGroup, espacio: float = 1.0, alineacion: str = "centro", 
                      max_abajo: float = -3, max_arriba: float = 3, desplazamiento_horizontal: float = 0) -> VGroup:
    """
    Distribuye un grupo de objetos en línea vertical con espacio uniforme dentro de límites,
    considerando el tamaño total de los objetos. También permite mover el grupo horizontalmente
    según el parámetro desplazamiento_x.

    Parámetros:
    - grupo: VGroup con los objetos a distribuir
    - espacio: distancia vertical entre objetos
    - alineacion: 'centro', 'abajo' o 'arriba'
    - max_abajo: límite inferior del área de distribución
    - max_arriba: límite superior del área de distribución
    - desplazamiento_x: valor para mover el grupo en el eje X (positivo para derecha, negativo para izquierda)

    Retorna:
    - El mismo grupo, con objetos reposicionados
    """
    n = len(grupo)

    # Calcular la altura total que ocuparán los objetos (considerando el espacio entre ellos)
    altura_total_objetos = sum([objeto.height for objeto in grupo]) + (n - 1) * espacio

    # Calcular un factor de desplazamiento proporcional al espacio vertical disponible
    factor_desplazamiento = max(0.5, (max_arriba - max_abajo) / altura_total_objetos)

    # Calcular cuánto puede desplazarse el grupo hacia arriba o abajo
    desplazamiento_max_abajo = (max_abajo + altura_total_objetos / 2) * factor_desplazamiento
    desplazamiento_max_arriba = (max_arriba - altura_total_objetos / 2) * factor_desplazamiento

    # Colocar los objetos en línea vertical
    for i, obj in enumerate(grupo):
        obj.move_to([0, -i * espacio, 0])

    # Alineación vertical
    if alineacion == "centro":
        desplazamiento = (desplazamiento_max_arriba - desplazamiento_max_abajo - altura_total_objetos) / 2
        grupo.shift(UP * (desplazamiento + desplazamiento_max_abajo))

    elif alineacion == "abajo":
        grupo.shift(DOWN * desplazamiento_max_abajo)

    elif alineacion == "arriba":
        grupo.shift(UP * desplazamiento_max_arriba)

    # Desplazamiento horizontal si se desea
    grupo.shift(RIGHT * desplazamiento_horizontal)

    return grupo

