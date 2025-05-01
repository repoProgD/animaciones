from manim import *

class NodoCircuito(VGroup):
    class NodoCircuito(VGroup):
        """
        NodoCircuito representa una unidad gráfica compuesta por un nodo circular y una o dos líneas conectadas,
        útil para diagramas de circuitos, redes o decoraciones técnicas.

        Parámetros:
        ----------
        radio : float
            Radio del círculo central (nodo).
        largo : float
            Longitud de la primera línea conectada al nodo.
        angulo : float
            Rotación general de todo el conjunto (en grados).
        segunda_linea : bool
            Si es True, agrega una segunda línea conectada al extremo de la primera.
        angulo_salida : float
            Ángulo (0–360°) desde donde sale la primera línea, medido desde el centro del círculo.
        angulo_segunda : float
            Ángulo absoluto (0–360°) de la segunda línea respecto al eje horizontal.
        largo_segunda : float or None
            Longitud de la segunda línea. Si es None, se usa el mismo largo que la primera.
        color : Manim Color
            Color del trazo del nodo y las líneas.
        relleno : bool
            Si es True, el círculo se rellena con el mismo color.
        opacidad_relleno : float
            Nivel de opacidad del relleno del círculo (0 a 1).
        kwargs : dict
            Otros parámetros opcionales para VGroup.
        """

    def __init__(self, 
                 radio=0.1, 
                 largo=0.5, 
                 angulo=0, 
                 segunda_linea=False, 
                 angulo_salida=0,
                 angulo_segunda=90,
                 largo_segunda=None,
                 color=WHITE,
                 relleno=False,
                 opacidad_relleno=1.0,
                 **kwargs):
        super().__init__(**kwargs)

        # Nodo central
        nodo = Circle(radius=radio, color=color)
        if relleno:
            nodo.set_fill(color, opacity=opacidad_relleno)
        else:
            nodo.set_fill(opacity=0)

        # Punto de salida según ángulo
        salida_rad = np.radians(angulo_salida)
        direccion_salida = np.array([np.cos(salida_rad), np.sin(salida_rad), 0])
        punto_salida = nodo.get_center() + direccion_salida * radio

        # Línea principal en esa dirección
        linea1 = Line(
            start=punto_salida,
            end=punto_salida + direccion_salida * largo,
            color=color
        )
        
        self.extremo = linea1.get_end()

        self.add(nodo, linea1)

        if segunda_linea:
            largo2 = largo_segunda if largo_segunda is not None else largo
            origen_segunda = linea1.get_end()

            # Ángulo de la segunda línea relativo a la horizontal
            ang2_rad = np.radians(angulo_segunda)
            direccion2 = np.array([np.cos(ang2_rad), np.sin(ang2_rad), 0])

            linea2 = Line(
                start=origen_segunda,
                end=origen_segunda + direccion2 * largo2,
                color=color
            )
            self.add(linea2)

        # Rotar todo si se desea
        self.rotate(np.radians(angulo))