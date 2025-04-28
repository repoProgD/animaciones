from manim import *

class TextWidgetPanel(VGroup):
    def __init__(self, text: str, alignment="center", padding=0.2, fill=False, fill_color=BLUE, opacity=1,
                 container_type="Rectangle", corner_radius=0.2, **kwargs):
        super().__init__(**kwargs)
        
        # Crear el texto
        self.text = Text(text)
        
        # Crear el contenedor con el tipo solicitado
        if container_type == "Rectangle":
            self.container = Rectangle(
                width=self.text.width + 2 * padding,  # Añadir espacio alrededor del texto
                height=self.text.height + 2 * padding,
                color=WHITE,
                fill_color=fill_color if fill else None,  # Usar fill_color si 'fill' es True
                fill_opacity=opacity,
            )
        elif container_type == "RoundedRectangle":
            self.container = RoundedRectangle(
                width=self.text.width + 2 * padding,  # Añadir espacio alrededor del texto
                height=self.text.height + 2 * padding,
                color=WHITE,
                fill_color=fill_color if fill else None,  # Usar fill_color si 'fill' es True
                fill_opacity=opacity,
                corner_radius=corner_radius  # Radio de los bordes redondeados
            )

        # Alineación del texto
        if alignment == "center":
            # Centrar el texto en el contenedor
            self.text.move_to(self.container.get_center())
        elif alignment == "left":
            # Calcular desplazamiento para la alineación a la izquierda
            text_right = self.text.get_right()[0]
            container_left = self.container.get_right()[0]
            distance = text_right - container_left
            displacement = distance * 0.6  # 60% del espacio entre el texto y el borde
            self.text.shift(RIGHT * displacement)
        elif alignment == "right":
            # Calcular desplazamiento para la alineación a la derecha
            text_left = self.text.get_left()[0]
            container_right = self.container.get_left()[0]
            distance = container_right - text_left
            displacement = distance * 0.6  # 60% del espacio entre el texto y el borde
            self.text.shift(LEFT * displacement)

        # Colocar el texto y el contenedor en el grupo
        self.add(self.container, self.text)
