from manim import *
import math

def copiar_adyacente(
    objeto: VMobject, 
    direccion: str, 
    espacio: float = 1.0, 
    max_izquierda: float = -7, 
    max_derecha: float = 7, 
    max_abajo: float = -4, 
    max_arriba: float = 4
) -> VMobject:
    """
    Crea una copia del objeto y la posiciona adyacente en la dirección especificada,
    respetando el espacio dado y los límites del área visible.

    Parámetros:
    - objeto: el VMobject que se va a copiar
    - direccion: 'arriba', 'abajo', 'izquierda', 'derecha'
    - espacio: distancia entre el objeto original y la copia
    - max_izquierda, max_derecha, max_abajo, max_arriba: límites del frame

    Retorna:
    - La copia posicionada, o None si no cabe dentro de los límites.
    """
    # Crear copia
    copia = objeto.copy()
    
    # Calcular el desplazamiento basado en el tamaño del objeto y el espacio deseado
    dx = objeto.width / 2 + espacio + copia.width / 2
    dy = objeto.height / 2 + espacio + copia.height / 2

    # Decidir el desplazamiento según la dirección
    if direccion == "arriba":
        copia.next_to(objeto, UP, buff=espacio)
    elif direccion == "abajo":
        copia.next_to(objeto, DOWN, buff=espacio)
    elif direccion == "izquierda":
        copia.next_to(objeto, LEFT, buff=espacio)
    elif direccion == "derecha":
        copia.next_to(objeto, RIGHT, buff=espacio)
    else:
        raise ValueError("Dirección inválida. Usa 'arriba', 'abajo', 'izquierda' o 'derecha'.")

    # Verificar que la copia quede dentro de los límites
    x, y, _ = copia.get_center()
    if (x - copia.width/2 < max_izquierda or
        x + copia.width/2 > max_derecha or
        y - copia.height/2 < max_abajo or
        y + copia.height/2 > max_arriba):
        return None  # No se puede colocar

    return copia



def copiar_en_angulo(
    objeto: VMobject,
    angulo_grados: float,
    distancia: float = 1.0,
    max_izquierda: float = -7,
    max_derecha: float = 7,
    max_abajo: float = -4,
    max_arriba: float = 4
) -> VMobject:
    """
    Crea una copia del objeto y la posiciona en la dirección especificada por un ángulo,
    respetando la distancia dada (de centro a centro) y los límites del área visible.

    Parámetros:
    - objeto: el VMobject que se va a copiar
    - angulo_grados: ángulo de colocación (0° a 359°), donde 0° es derecha, 90° es arriba
    - distancia: distancia entre el centro del objeto original y el centro de la copia
    - max_izquierda, max_derecha, max_abajo, max_arriba: límites del frame

    Retorna:
    - La copia posicionada, o None si no cabe dentro de los límites.
    """
    copia = objeto.copy()

    # Normalizar el ángulo a [0, 360)
    angulo_grados = angulo_grados % 360

    # Convertir ángulo a radianes
    angulo_radianes = math.radians(angulo_grados)

    # Calcular desplazamiento
    dx = distancia * math.cos(angulo_radianes)
    dy = distancia * math.sin(angulo_radianes)

    # Mover la copia
    copia.move_to(objeto.get_center() + np.array([dx, dy, 0]))

    # Verificar que esté dentro de los límites
    x, y, _ = copia.get_center()
    if (x - copia.width/2 < max_izquierda or
        x + copia.width/2 > max_derecha or
        y - copia.height/2 < max_abajo or
        y + copia.height/2 > max_arriba):
        return None

    return copia

def copiar_en_circulo(
    objeto: VMobject,
    cantidad: int,
    radio: float = 2.0,
    max_izquierda: float = -7,
    max_derecha: float = 7,
    max_abajo: float = -4,
    max_arriba: float = 4
) -> VGroup:
    """
    Crea múltiples copias del objeto distribuidas uniformemente en un círculo.

    Parámetros:
    - objeto: el VMobject que se va a copiar
    - cantidad: número de copias a generar
    - radio: distancia del centro del objeto original a cada copia
    - max_izquierda, max_derecha, max_abajo, max_arriba: límites del frame

    Retorna:
    - Un VGroup con todas las copias posicionadas (no incluye el objeto original)
    """
    copias = VGroup()

    for i in range(cantidad):
        angulo = (360 / cantidad) * i
        copia = copiar_en_angulo(
            objeto=objeto,
            angulo_grados=angulo,
            distancia=radio,
            max_izquierda=max_izquierda,
            max_derecha=max_derecha,
            max_abajo=max_abajo,
            max_arriba=max_arriba
        )
        if copia:
            copias.add(copia)

    return copias
