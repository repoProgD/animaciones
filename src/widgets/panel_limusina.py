from manim import *

class PanelLimusina(VGroup):
    def __init__(self, text: Text, alignment="center", padding=0.8, fill=False, fill_color=BLUE, opacity=1,
                 corte=0.3, **kwargs):
        super().__init__(**kwargs)
        
        # Usamos el objeto Text directamente en lugar de crear uno nuevo
        self.text = text

        # Calcular dimensiones del panel basadas en el texto
        width = self.text.width + 2 * padding
        height = self.text.height + 1.25 * padding

        # Asegurar que el corte no sea demasiado grande para las dimensiones
        corte = min(corte, width / 2 - 0.01, height / 2 - 0.01)

        # Definir los 8 puntos del octágono limusina
        puntos = [
            [-width/2 + corte, height/2, 0],         # Punto 1 (esquina sup izq)
            [width/2 - corte, height/2, 0],          # Punto 2
            [width/2, height/2 - corte, 0],          # Punto 3
            [width/2, -height/2 + corte, 0],         # Punto 4
            [width/2 - corte, -height/2, 0],         # Punto 5
            [-width/2 + corte, -height/2, 0],        # Punto 6
            [-width/2, -height/2 + corte, 0],        # Punto 7
            [-width/2, height/2 - corte, 0],         # Punto 8
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

        # Agregar elementos al grupo
        self.add(self.container, self.text)