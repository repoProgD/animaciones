from manim import *
import herramientas as h
import funciones as f
from config_vertical import FRAME_HEIGHT, FRAME_WIDTH

config.media_width = "75%"
#config.verbosity = "WARNING" # Esto es solo para Jupyter Notebook
config.background_color = "#24043d"


 
class MetodosCadenas(Scene):  # ¡Esto es clave! esta clase hereda a Scene, en teoría puedo hacer todo lo mismo
    def construct(self):
        # 1. Setear formato vertical 9:16
        #self.camera.frame.set(width=9, height=16)

        # 2. Zoom out para más espacio de trabajo
        #self.camera.frame.scale(1)

        # 3. Agregar rejilla
        h.toggle_grilla(self, mostrar=False)
        # 4 Agregar logo
        logo = h.LogoV()
        self.add(logo)

        self.wait(2)
        
         # Crear y agregar título
        titulo = Text("Métodos de cadenas(Strings)").move_to(6.5 * UP).scale(0.825)
        subrayado = Underline(titulo)
        self.play(Write(titulo), Write(subrayado))
        self.wait(2)
        
        ###########  El resto de la escena

        def crear_snippet(codigo):
            """Crea una ventana de código y lo muestra palabra por palabra"""
            self.play(Create(codigo[0]))
            for i in range(len(codigo[2])):
                chars_por_seg = len(codigo[2][i])/4
                self.play(FadeIn(codigo[1][i]))
                self.play(AddTextLetterByLetter(codigo[2][i]), run_time=chars_por_seg, rate_func=linear)
            self.wait(1)

        def crear_contenedores(un_texto):      
            cuadrados = VGroup(*[Square(side_length=0.65,
                                fill_color=PINK,
                                fill_opacity=0.95,
                                stroke_width=1) for i in range(len(un_texto))])
            cuadrados.arrange_in_grid(rows=1, buff=0.1)
            return cuadrados
         
        def alinear_letras(un_texto, contenedores):
            # Alinear horizontalmente las letras con la parte inferior de los cuadrados
            for letra, cuadrado in zip(un_texto, contenedores):
                letra.move_to(cuadrado.get_bottom(), aligned_edge=DOWN)
            un_texto.shift(0.08 * UP)

        def crear_codigo(un_texto):
            codigo = Code(code = un_texto, tab_width = 7.5, background = "window",language = "Python", font="Monospace", font_size=38)
            return codigo
        # Obtener el tamaño de la pantalla
        ancho = self.camera.frame_width
        alto = self.camera.frame_height

        mi_texto = """
cadena = 'mi cadena'
cadena.upper()"""
        
        texto_interno = Text("mi.cadena").scale(0.95)
    
        codigo = crear_codigo(mi_texto).move_to([0,3.5,0])
        crear_snippet(codigo)

        contenedores = crear_contenedores(texto_interno).move_to(2.5*DOWN)
        contenedores[2].set_z_index(500)
        # Alinear horizontalmente las letras con la parte inferior de los cuadrados
        alinear_letras(texto_interno, contenedores)
        # Crear un subtítulo explicativo
        explicacion = Text("Convierte el texto en mayúsculas").scale(0.7).next_to(contenedores.get_top() + 1.5 * UP + 4.25 * LEFT)
        # Agregar los contenedores y el texto a la escena
        self.play(FadeIn(contenedores, run_time=1))
        self.wait(1)
        self.play(Write(texto_interno, run_time=1.5))
        self.play(Write(explicacion))      
        # a mayúsculas
        to_upper = Text("MI_CADENA").scale(0.95)
        alinear_letras(to_upper, contenedores)      
        # Indicar
        for i in range(2):
            self.play(Circumscribe(contenedores[0]), Circumscribe(contenedores[1]), Circumscribe(contenedores[3]),
                 Circumscribe(contenedores[4]),Circumscribe(contenedores[5]),Circumscribe(contenedores[6]),Circumscribe(contenedores[7]),
                 Circumscribe(contenedores[8]))
        self.play(Transform(texto_interno, to_upper))
        self.remove(texto_interno[2])
        self.play(Unwrite(explicacion))  
 
        mi_texto2 = """
cadena = 'MI CADENA'
cadena.lower()"""
        explicacion2 = Text("Convierte el texto en minúsculas").scale(0.7).next_to(contenedores.get_top() + 1.5 * UP + 4.25 * LEFT)
        to_lower = Text("mi_cadena").scale(0.95)

        codigo2 = crear_codigo(mi_texto2).move_to([0,3.5,0])
        crear_snippet(codigo2)

        alinear_letras(to_lower, contenedores)

        self.play(Write(explicacion2))
        # Indicar
        for i in range(2):
            self.play(Circumscribe(contenedores[0]), Circumscribe(contenedores[1]), Circumscribe(contenedores[3]),
                 Circumscribe(contenedores[4]),Circumscribe(contenedores[5]),Circumscribe(contenedores[6]),Circumscribe(contenedores[7]),
                 Circumscribe(contenedores[8]))
        # Transformar     
        self.play(Transform(texto_interno, to_lower))
        self.remove(texto_interno[2])
        self.play(Unwrite(explicacion2))
        # capitalize
        mi_texto3 = """
cadena = 'mi cadena'
cadena.capitalize()"""
        explicacion3 = Text("Convierte en mayúscula solamente\nla primera letra del texto").scale(0.7).next_to(contenedores.get_top() + 1.5 * UP + 4.25 * LEFT)
        capitalizar = Text("Mi_cadena").scale(0.95)

        codigo3 = crear_codigo(mi_texto3).move_to([0,3.5,0])
        crear_snippet(codigo3)

        alinear_letras(capitalizar, contenedores)

        self.play(Write(explicacion3))
        # Indicar
        for i in range(2):
            self.play(Circumscribe(contenedores[0]))
        # Transformar
        self.play(Transform(texto_interno, capitalizar))
        self.remove(texto_interno[2]) 
        self.play(Unwrite(explicacion3))

        mi_texto4 = """
cadena = 'Mi cadena'
cadena.title()"""
        explicacion4 = Text("Convierte en mayúscula a\ncada primera letra del texto").scale(0.7).next_to(contenedores.get_top() + 1.5 * UP + 4.25 * LEFT)
        title = Text("Mi_Cadena").scale(0.95)

        codigo4 = crear_codigo(mi_texto4).move_to([0,3.5,0])
        crear_snippet(codigo4)

        alinear_letras(title, contenedores)

        self.play(Write(explicacion4))
        # Indicar
        for i in range(2):
            self.play(Circumscribe(contenedores[0]), Circumscribe(contenedores[3]))
        # Transformar
        self.play(Transform(texto_interno, title))
        self.remove(texto_interno[2])
        self.play(Unwrite(explicacion4))
   
        self.wait(3)
        
        #### strip
        # crear contenedores extra
        contenedor_ini = contenedores[0].copy().set_z_index(-1)
        contenedor_ini2 = contenedores[0].copy().set_z_index(-2)
        contenedor_ini3 = contenedores[0].copy().set_z_index(-3)
        contenedor_fin = contenedores[-1].copy().set_z_index(-4)
        contenedor_fin2 = contenedores[-1].copy().set_z_index(-5)
        contenedor_fin3 = contenedores[-1].copy().set_z_index(-6)
        # strip
        mi_texto5 = """
cadena = ' Mi Cadena '
cadena.strip()"""
        
        explicacion5 = Text("Remueve espacios en blanco\n en los extremos").scale(0.7).next_to(contenedores.get_top() + 1.5 * UP + 4.25 * LEFT)
         
        codigo5 = crear_codigo(mi_texto5).move_to([0,3.5,0])
        crear_snippet(codigo5)
        
        self.play(contenedor_ini.animate.shift(LEFT * 0.8), contenedor_fin.animate.shift(RIGHT * 0.8))
        self.play(Write(explicacion5))
        for i in range(2):
            self.play(Circumscribe(contenedor_ini), Circumscribe(contenedor_fin))
        self.play(Unwrite(contenedor_ini), Unwrite(contenedor_fin), Unwrite(explicacion5))

        self.wait(2)
       
        # rstrip
        mi_texto6 = """
cadena = 'Mi Cadena  '
cadena.rstrip()"""
        self.play(contenedores.animate.shift(1*LEFT), texto_interno.animate.shift(1*LEFT))
        self.wait(1)
        explicacion6 = Text("Remueve espacios en blanco\n al final de la cadena").scale(0.7).next_to(contenedores.get_top() + 1.5 * UP + 4.25 * LEFT) 
        
        codigo6 = crear_codigo(mi_texto6).move_to([0,3.5,0])
        crear_snippet(codigo6)

        self.play(contenedor_fin2.animate.shift(0.5 * RIGHT), contenedor_fin3.animate.shift(0.25 * LEFT))
        self.play(Write(explicacion6))
        for i in range(2):
            self.play(Circumscribe(contenedor_fin2), Circumscribe(contenedor_fin3))
        self.play(Uncreate(contenedor_fin2), Uncreate(contenedor_fin3), Unwrite(explicacion6))
        self.wait(3)

        mi_texto7 = """
cadena = '  Mi Cadena'
cadena.lstrip()"""
        self.play(contenedores.animate.shift(2*RIGHT), texto_interno.animate.shift(2*RIGHT))
        self.wait(1)
        explicacion7 = Text("Remueve espacios en blanco\nal inicio de la cadena").scale(0.7).next_to(contenedores.get_top() + 1.5 * UP + 4.25 * LEFT) 
        
        codigo7 = crear_codigo(mi_texto7).move_to([0,3.5,0])
        crear_snippet(codigo7)

        self.play(contenedor_ini2.animate.shift(0.25 * RIGHT), contenedor_ini3.animate.shift(0.5 * LEFT))
        self.play(Write(explicacion7))
        for i in range(2):
            self.play(Circumscribe(contenedor_ini2), Circumscribe(contenedor_ini3))
        self.play(Uncreate(contenedor_ini2), Uncreate(contenedor_ini3), Unwrite(explicacion7))
        self.wait(3)
