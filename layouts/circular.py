from manim import *

def en_circulo(grupo: VGroup, radio: float = 3.0, espacio: float = 1.0, alineacion: str = "centro", altura: float = 0) -> VGroup:
    """
    Distribuye un grupo de objetos en una circunferencia.

    Parámetros:
    - grupo: VGroup con los objetos a distribuir
    - radio: radio de la circunferencia en la que se distribuirán los objetos
    - espacio: espacio angular entre los objetos (en radianes)
    - alineacion: 'centro', 'izquierda' o 'derecha'
    - altura: ajuste vertical para mover todo el grupo hacia arriba o abajo

    Retorna:
    - El mismo grupo, con objetos reposicionados
    """
    n = len(grupo)  # Número de objetos a distribuir
    angulo_total = 2 * PI  # Un círculo completo

    # Calcular el espacio angular entre cada objeto
    espacio_angular = angulo_total / n

    # Colocar los objetos a lo largo de la circunferencia
    for i, obj in enumerate(grupo):
        angulo = i * espacio_angular
        obj.move_to([radio * np.cos(angulo), radio * np.sin(angulo), 0])

    # Ajustar la altura de todo el grupo
    grupo.shift(UP * altura)

    # Alineación del grupo
    if alineacion == "centro":
        grupo.move_to(ORIGIN)
    elif alineacion == "izquierda":
        grupo.shift(LEFT * radio)
    elif alineacion == "derecha":
        grupo.shift(RIGHT * radio)

    return grupo
