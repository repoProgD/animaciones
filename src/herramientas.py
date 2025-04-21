from manim import *

class Logo(VMobject):
    def __init__(self, **kwargs):
        # inicializar el VMobject
        super().__init__(**kwargs)
        logo = ImageMobject("..\\images\\logorobo.png").scale(0.65)
        logo.move_to(DOWN * 2.8 + LEFT * 5.9).set_opacity(0.55)
        self.add(logo)

class CrearSecuencia(VMobject):  
    def __init__(self, figura, tamanio, cantidad, inicio, hacia, objetos_adicionales=None, espaciado=0.1, **kwargs):
        """ 
        figura = tipo de figura u objeto(Texto, Imagen, Square, etc); tamanio = tamaño de un lado, radio, etc;
        cantidad = cantidad de objetos de la secuencia; inicio = lugar donde se ubica el primer objeto; hacia = dirección hacia donde va la secuencia;
        objetos_adicionales = lista de objetos a agregar en el centro de cada elemento de la secuencia original;
        espaciado = espaciado entre objetos de la secuencia. 
        La secuencia puede direccionarse hacia cualquier parte de la screen cambiando el parámetro "hacia"
        """
        # initialize the vmobject
        super().__init__(**kwargs)
        
        grupo_unidades = VGroup()
        
        for i in range(cantidad):
            nueva_figura = figura.copy()
            nueva_figura.move_to(inicio * 1.5 + i * (tamanio + espaciado) * hacia)
            
            # Agregar objeto adicional en el centro de la figura y formar una unidad
            if objetos_adicionales is not None:
                objeto_adicional = objetos_adicionales[i].copy()
                objeto_adicional.move_to(nueva_figura.get_center())
                unidad = VGroup(nueva_figura, objeto_adicional)
                grupo_unidades.add(unidad)
            else:
                grupo_unidades.add(nueva_figura)
        
        # Agregar el grupo de unidades a la escena
        self.add(grupo_unidades)
        
class Stack(VMobject):
    def __init__(self, size, **kwargs):
        # initialize the vmobject
        super().__init__(**kwargs)

        self.squares = VGroup()
        self.labels = VGroup()
        self.index = 0
        self.pointer = Arrow(ORIGIN, UP * 1.2)

        for _ in range(size):
            self.squares.add(Square(side_length=0.8))

        self.squares.arrange(buff=0.15)

        self.pointer.next_to(self.squares[0], DOWN)

        # Importante: hay que agregar todos los subobjetos para que se puedan mostrar
        self.add(self.squares, self.pointer, self.labels)

class GrillaRegla(VMobject):
    """Crea una grilla en toda la pantalla que sirve para ubicar objetos alineadamente"""
    def __init__(self, **kwargs):
        # inicializar el VMobject
        super().__init__(**kwargs)
    
        ancho = 14.22
        alto = 8
        separacion_vertical = ancho / 14
        separacion_horizontal = 1

        # Dibujar líneas horizontales
        for i in range(9):
            y = -alto / 2 + i * separacion_horizontal
            linea_horizontal = Line(
                start=LEFT * ancho / 2,
                end=RIGHT * ancho / 2,
                color=WHITE
            )
            linea_horizontal.move_to(UP * y)
            self.add(linea_horizontal)

        # Dibujar líneas verticales
        for i in range(15):
            x = -ancho / 2 + i * separacion_vertical
            linea_vertical = Line(
                start=UP * alto / 2,
                end=DOWN * alto / 2,
                color=WHITE
            )
            linea_vertical.move_to(RIGHT * x)
            self.add(linea_vertical)

class Reglas(VMobject):
    """Reglas individuales para alinear los objetos en pantalla"""
    def __init__(self, **kwargs):
        # inicializar el VMobject
        super().__init__(**kwargs)
        punto1 = Point(4 * DOWN)
        punto2 = Point(4 * UP)
        punto3 = Point(7.11 * LEFT)
        punto4 = Point(7.11 * RIGHT)
        linea_v = Line(punto1, punto2)
        linea_h = Line(punto3, punto4)
        self.add(linea_v, linea_h)


####################################  ##################################



