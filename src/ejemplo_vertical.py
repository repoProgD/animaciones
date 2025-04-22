from manim import *
import herramientas as h
import funciones as f
from config_vertical import FRAME_HEIGHT, FRAME_WIDTH

# # Swap para el intercambio de pixeles (cambio de resolución, disponemos los píxeles en formato vertical)
# altura_default = config.pixel_height
# config.pixel_height = config.pixel_width
# config.pixel_width = altura_default

# # Cambio del frame para ajustarse al cambio de resolución
# config.frame_width = config.frame_height * (9/16)
# FRAME_HEIGHT = config.frame_height
# FRAME_WIDTH = config.frame_width

config.media_width = "75%"
config.verbosity = "WARNING"
config.background_color = "#24043d"

class Ejemplo(Scene):

    def construct(self):
        # Añadir logo
        logo = h.LogoV()
        self.add(logo)


        def crear_contenedores(un_texto):      
            cuadrados = VGroup(*[Square(side_length=0.5,
                                fill_color=PINK,
                                fill_opacity=0.95,
                                stroke_width=2) for i in range(len(un_texto))])
            cuadrados.arrange_in_grid(rows=1, buff=0.1)
            return cuadrados
         
        def alinear_letras(un_texto, contenedores):
            # Alinear horizontalmente las letras con la parte inferior de los cuadrados
            for letra, cuadrado in zip(un_texto, contenedores):
                letra.move_to(cuadrado.get_bottom(), aligned_edge=DOWN)
            un_texto.shift(0.2 * UP)

        # Obtener el tamaño de la pantalla
        ancho = self.camera.frame_width
        alto = self.camera.frame_height


        # Obtener el tamaño de la pantalla
        ancho = self.camera.frame_width
        alto = self.camera.frame_height

        #grilla = h.GrillaRegla()
        #self.add(grilla)

        mi_texto = """
cadena = 'Hola mundo!'
cadena.upper()"""
        texto_interno = Text("hola.mundo!")
    
        codigo = f.crear_codigo(mi_texto, 2 * DOWN)
        f.generar_snippet(self, codigo)
        #resultado = Rectangle(width=5.5, height=1.25, fill_color=BLACK,fill_opacity=0.75, stroke_width=2)
        #resultado.move_to(4 * LEFT + 1 * UP)
        
        contenedores = crear_contenedores(texto_interno)
        contenedores[4].set_z_index(500)
        # Alinear horizontalmente las letras con la parte inferior de los cuadrados
        alinear_letras(texto_interno, contenedores)
        # Agregar los contenedores y el texto a la escena
        self.add(contenedores, texto_interno)
        self.remove(texto_interno[4])
        self.wait(4) 

