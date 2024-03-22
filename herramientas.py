from manim import *

class Logo(VMobject):
    def __init__(self, **kwargs):
        # inicializar el VMobject
        super().__init__(**kwargs)
        logo = ImageMobject("images\\logorobo.png").scale(0.65)
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

        # IMPORTANT - we have to add all of the subobjects for them to be displayed
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


#################################### Funciones ##################################

def get_x(coord_x):
    if coord_x < 0:
        return LEFT * abs(coord_x)
    else:
        return RIGHT * coord_x

def get_y(coord_y):
    if coord_y < 0:
        return DOWN * abs(coord_y)
    else:
        return UP * coord_y

def crear_codo(x_punto,  y_punto):
    coord_x = get_x(x_punto[0])
    coord_y = get_y(y_punto[1])
    punto_i = Point()
    punto_i.move_to(coord_x + coord_y)

    linea1 = Line(x_punto, punto_i)
    linea2 = Line(y_punto, punto_i)
    codo = VGroup(*[linea1, linea2])
    return codo

def crear_rectangulo(ancho, alto, color, opacidad, texto):
            # Crear rectángulo con esquinas redondeadas
            rectangulo = RoundedRectangle(corner_radius=0.1, width=ancho, height=alto).set_fill(color=color, opacity=opacidad)
            # Crear texto
            texto_obj = Text(texto).scale(0.5).move_to(rectangulo.get_center())
            # Agrupar rectángulo y texto
            grupo = Group(rectangulo, texto_obj)
            return grupo

def get_nearest_point(a, b, p):
    """Recibe 3 puntos del espacio R3. Los puntos a y b pertenecen a una recta.
    Mientras que el punto p está fuera de esta. 
    Retorna el punto perteneciente a la recta más cercano al punto p."""
    # Calcular el vector dirección de la recta
    vector_director = b - a
    # Calcular un vector que conecta el punto dado con un punto en la recta
    vector_conexion = p - a
    # Calcular la proyección de este vector sobre el vector dirección de la recta
    producto_escalar = np.dot(vector_conexion, vector_director)
    longitud_director_cuadrado = np.dot(vector_director, vector_director)
    proyeccion = (producto_escalar / longitud_director_cuadrado) * vector_director
    # Calcular el punto más cercano en la recta al punto dado
    punto_mas_cercano = a + proyeccion
    return a + proyeccion
            
def proliferar(secuencia):
    """Toma el primer valor de una secuencia, lo clona y lo replica en el resto de la secuencia"""
    for i in range(len(secuencia)-1, 0, -1):
    # Copiar el valor actual
        copia = secuencia[i].copy()
    # Desplazar la copia a la posición del índice anterior
        copia.move_to(secuencia[i-1].get_center())
    # Transformar el valor actual en la copia
        self.play(Transform(secuencia[i-1], copia), run_time=0.5)  