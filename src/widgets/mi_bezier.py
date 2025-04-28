
"""
    Un widget de Manim que visualiza una curva de Bézier cúbica y sus puntos de control.

    Este widget permite crear una curva de Bézier cúbica a partir de cuatro puntos de control
    (p0, p1, p2, p3), representando tanto los puntos como la curva. Además, incluye la capacidad
    de actualizar las posiciones de los puntos de control y recalcular la curva en tiempo real.

    Atributos:
        p0, p1, p2, p3 (np.array): Puntos de control que definen la curva de Bézier.
        bezier_curve (CubicBezier): Objeto de la curva de Bézier basado en los puntos de control.
        control_points (VGroup): Un grupo de puntos visuales que representan los puntos de control.
        labels (VGroup): Un grupo de etiquetas para los puntos de control.

    Métodos:
        __init__(p0, p1, p2, p3, **kwargs): Inicializa el widget con los puntos de control dados.
        update_points(p0=None, p1=None, p2=None, p3=None): Actualiza las posiciones de los puntos de control
                                                          y recalcula la curva de Bézier con las nuevas posiciones.

    Uso:
        # Crear una instancia del widget
        bezier_widget = BezierCurveWidget(p0, p1, p2, p3)

        # Para actualizar los puntos y la curva
        bezier_widget.update_points(p0=new_p0, p1=new_p1)
"""


from manim import *

class BezierCurveWidget(VGroup):      
    def __init__(self, p0, p1, p2, p3, **kwargs):
        super().__init__(**kwargs)

        # Definir los puntos de control como vectores [x, y, z]
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # Crear la curva de Bézier cúbica
        self.bezier_curve = CubicBezier(self.p0, self.p1, self.p2, self.p3, color=BLUE)

        # Crear los puntos de control (círculos)
        self.control_points = VGroup(
            Dot(self.p0, color=RED),
            Dot(self.p1, color=RED),
            Dot(self.p2, color=RED),
            Dot(self.p3, color=RED)
        )

        # Etiquetas para los puntos de control
        self.labels = VGroup(
            Tex("$P_0$").next_to(self.p0, DOWN),
            Tex("$P_1$").next_to(self.p1, LEFT),
            Tex("$P_2$").next_to(self.p2, RIGHT),
            Tex("$P_3$").next_to(self.p3, DOWN)
        )

        # Añadir la curva, los puntos de control y las etiquetas al widget
        self.add(self.bezier_curve, self.control_points, self.labels)

    def update_points(self, p0=None, p1=None, p2=None, p3=None):
        """Actualiza la posición de los puntos de control y la curva"""
        if p0 is not None:
            self.p0 = p0
            self.control_points[0].move_to(p0)
        if p1 is not None:
            self.p1 = p1
            self.control_points[1].move_to(p1)
        if p2 is not None:
            self.p2 = p2
            self.control_points[2].move_to(p2)
        if p3 is not None:
            self.p3 = p3
            self.control_points[3].move_to(p3)

        # Actualizar la curva de Bézier
        self.bezier_curve = CubicBezier(self.p0, self.p1, self.p2, self.p3, color=BLUE)
        self[0] = self.bezier_curve  # Reemplazar la curva anterior