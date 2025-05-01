from manim import *

class PanelEnPunta(VGroup):
    def __init__(
        self,
        text_object: Text,  # Objeto de texto pasado directamente
        alignment="center",
        padding=0.4,
        fill=False,
        fill_color=BLUE,
        opacity=1,
        corte=2,  # El tamaño del corte para las esquinas
        **kwargs
    ):
        super().__init__(**kwargs)
        
        # El objeto Text ya está pasado directamente, no hace falta crearlo de nuevo
        self.text = text_object

        # Calcular dimensiones del panel basadas en el objeto de texto
        width = self.text.width + 2 * padding
        height = self.text.height + 2 * padding

        # Asegurarse de que el corte no sea mayor que la mitad del ancho o alto
        corte = min(corte, width / 2 - 0.01, height / 2 - 0.01)

        # Aquí definimos correctamente los puntos del octágono limusina
        puntos = [
            [-width/2 + corte, height/2, 0],         # Esquina superior izquierda
            [width/2 - corte, height/2, 0],          # Esquina superior derecha
            [width/2, height/2 - corte, 0],          # Esquina superior derecha (corte)
            [width/2, -height/2 + corte, 0],         # Esquina inferior derecha (corte)
            [width/2 - corte, -height/2, 0],         # Esquina inferior derecha
            [-width/2 + corte, -height/2, 0],        # Esquina inferior izquierda
            [-width/2, -height/2 + corte, 0],        # Esquina inferior izquierda (corte)
            [-width/2, height/2 - corte, 0],         # Esquina superior izquierda (corte)
        ]

        # Crear el contorno del panel como un polígono
        self.container = Polygon(
            *puntos,
            color=WHITE,
            fill_color=fill_color if fill else None,
            fill_opacity=opacity,
            stroke_width=2
        )

        # Alineación del texto
        if alignment == "center":
            self.text.move_to(self.container.get_center())
        elif alignment == "left":
            self.text.next_to(self.container.get_left(), RIGHT, buff=padding / 2)
        elif alignment == "right":
            self.text.next_to(self.container.get_right(), LEFT, buff=padding / 2)

        # Agregar los elementos al grupo
        self.add(self.container, self.text)