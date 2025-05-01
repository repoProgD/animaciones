from manim import *

class CurvaAnimada:
    """
    Representa una animación de un punto (Dot) que se desplaza a lo largo de una trayectoria, dejando un trazo visible.

    Esta clase encapsula el comportamiento de animar un punto que sigue una curva dada
    (por ejemplo, una espiral o cualquier `VMobject`) y dibuja el recorrido que realiza.

    Atributos:
    ----------
    trayectoria : VMobject
        La curva sobre la cual se moverá el punto.
    color : Color, opcional
        El color del punto y del trazo. Por defecto es WHITE.
    duracion : float, opcional
        Tiempo que dura la animación en segundos. Por defecto es 5.
    grosor : float, opcional
        Grosor del trazo que deja el punto. Por defecto es 4.

    Métodos:
    --------
    animar():
        Devuelve la animación que mueve el punto a lo largo de la trayectoria con una velocidad constante.
    """

    def __init__(self, trayectoria, color=WHITE, duracion=5, grosor=4):
        self.trayectoria = trayectoria
        self.color = color
        self.duracion = duracion
        self.grosor = grosor

        self.dot = Dot(self.trayectoria.get_start(), color=self.color)
        self.trazo = TracedPath(self.dot.get_center, stroke_color=self.color, stroke_width=self.grosor)

    def animar(self):
        return MoveAlongPath(self.dot, self.trayectoria, rate_func=linear, run_time=self.duracion)