from manim import *
import herramientas as h
import funciones as f
from config_vertical import FRAME_HEIGHT, FRAME_WIDTH

config.media_width = "75%"
#config.verbosity = "WARNING" # Esto es solo para Jupyter Notebook
config.background_color = "#24043d"


 
class Logo(Scene):  
    def construct(self):
        # 3. Agregar rejilla
        h.toggle_grilla(self, mostrar=False)
        # 4 Agregar logo
        logo = h.LogoV()
        self.add(logo)

        self.wait(2)