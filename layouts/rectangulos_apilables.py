from manim import *

class RectangulosApilables(VGroup):
    """
    Clase para organizar un conjunto de widgets rectangulares en una disposición vertical.
    
    Los widgets pueden alinearse al centro, a la izquierda o a la derecha del frame.
    La clase permite ajustar la separación vertical entre los widgets y aplicar desplazamientos
    horizontales, ya sea manualmente o aleatoriamente, según las necesidades del usuario.

    Parámetros:
    - widgets (list): Lista de objetos Manim (como Rectángulos o cualquier otra figura de Manim)
      que se alinearán en una pila vertical.
    - vertical_spacing (float, opcional): Espacio vertical entre los widgets (por defecto 0.5).
    - offsets_x (list de floats, opcional): Desplazamientos manuales en el eje X para cada widget.
      Si se define, reemplaza los desplazamientos aleatorios.
    - random_x_range (tuple de dos floats, opcional): Rango del desplazamiento aleatorio en el eje X,
      en caso de no usar `offsets_x`.
    - alignment (str, opcional): Controla la alineación de los widgets respecto al frame.
      Puede ser "center", "left" o "right" (por defecto "center").
    
    Métodos:
    - arrange_widgets(): Organiza los widgets en la escena, con la alineación y desplazamientos definidos.
    """

    def __init__(
        self,
        widgets,
        vertical_spacing=0.5,
        offsets_x=None,
        random_x_range=None,
        alignment="center",  # Puede ser "center", "left" o "right"
        **kwargs
    ):
        """
        Inicializa la clase RectangulosApilables.

        Parámetros:
        - widgets (list): Lista de widgets (pueden ser Rectángulos o cualquier figura de Manim).
        - vertical_spacing (float): Espacio vertical entre los widgets.
        - offsets_x (list de floats, opcional): Desplazamientos en el eje X para cada widget.
        - random_x_range (tuple de dos floats, opcional): Rango para desplazamientos aleatorios en X.
        - alignment (str): Alineación de los widgets respecto al frame (por defecto "center").
        """
        super().__init__(**kwargs)

        self.widgets = widgets
        self.vertical_spacing = vertical_spacing
        self.offsets_x = offsets_x
        self.random_x_range = random_x_range
        self.alignment = alignment

        self.arrange_widgets()

    def arrange_widgets(self):
        """
        Organiza los widgets verticalmente con los desplazamientos y alineaciones especificadas.

        El método mueve los widgets dentro de la escena, ajustando su posición en Y para apilarlos,
        y su posición en X según el parámetro de alineación y los desplazamientos horizontales 
        definidos (ya sea por `offsets_x` o `random_x_range`).
        """
        if not self.widgets:
            return

        frame_width = config.frame_width  # Usamos el ancho real del frame
        current_y = 0  # Vamos bajando en Y

        for i, widget in enumerate(self.widgets):
            widget.move_to(UP * current_y)

            # Cálculo del desplazamiento en X
            if self.offsets_x is not None:
                displacement_x = self.offsets_x[i]
                widget.shift(RIGHT * displacement_x)

            elif self.random_x_range is not None:
                displacement_x = random.uniform(*self.random_x_range)
                widget.shift(RIGHT * displacement_x)

            else:
                # Alineación manual respecto a los bordes del frame
                if self.alignment == "left":
                    widget.shift(LEFT * (frame_width / 2) + RIGHT * (widget.width / 2))
                elif self.alignment == "right":
                    widget.shift(RIGHT * (frame_width / 2) - RIGHT * (widget.width / 2))
                else:  # "center" (default)
                    pass  # ya está centrado naturalmente

            self.add(widget)

            # Actualizar la posición Y para el siguiente widget
            current_y -= (widget.height + self.vertical_spacing)