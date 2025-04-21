from manim import *
# Swap para el intercambio de pixeles (cambio de resolución, disponemos los píxeles en formato vertical)
altura_default = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = altura_default

# Cambio del frame para ajustarse al cambio de resolución
config.frame_width = config.frame_height * (9/16)
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class Ejemplo(Scene):
    def construct(self):
        texto5 = Text("Centro", color = WHITE)

        texto9 = Text("Arriba 4", color = WHITE).move_to(UP*4)
        texto8 = Text("Arriba 3", color = WHITE).move_to(UP*3)
        texto7 = Text("Arriba 2", color = WHITE).move_to(UP*2)
        texto6 = Text("Arriba 1", color = WHITE).move_to(UP)

        texto4 = Text("Abajo 1", color = WHITE).move_to(DOWN)
        texto3 = Text("Abajo 2", color = WHITE).move_to(DOWN*2)
        texto2 = Text("Abajo 3", color = WHITE).move_to(DOWN*3)
        texto1 = Text("Abajo 4", color = WHITE).move_to(DOWN*4)

        self.add(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8, texto9)
        self.wait(4) 
