from manim import *

class Funciones(Scene):


    def crear_contenedores(un_texto, color_trazo=WHITE, color=BLUE, lado=1.2, buff=0.1, trazo=2, opacity=1, **kwargs):
        """Crea una secuencia de figuras que sirven de contenedores para un texto.
        Hacemos uso de arrange_in_grid para que el texto quede contenido en cada una de las figuras."""
        cuadrados = VGroup(*[Square(side_length=lado,
                                color=color_trazo,
                                fill_color=color,
                                fill_opacity=1,
                                stroke_width=trazo) for i in range(len(un_texto))
                            ]
                           )
        cuadrados.arrange_in_grid(rows=1, buff=buff)
        return cuadrados
         
    def alinear_elementos(un_texto, contenedores):
        # Alinear horizontalmente las letras con la parte inferior de los cuadrados
        for letra, cuadrado in zip(un_texto, contenedores):
            letra.move_to(cuadrado.get_bottom(), aligned_edge=DOWN)
        un_texto.shift(0.2 * UP)
        
 
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
    """ Recibe dos puntos, idealmente del tipo numeros.get_top(), datos.get_left()
    para obtener las coordenadas de interés
    [0] indica el eje x por su posición en la lista de vectores[x, y, z]
    [1] indica el eje y"""
            
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
    rectangulo = RoundedRectangle(corner_radius=0.1, width=ancho,   height=alto).set_fill(color=color, opacity=opacidad)
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
            
def crear_puntos(puntos_posicion, cant_puntos=18, puntos_separacion=0.45):
    # Crear puntos
    puntos = VGroup(*[Dot(radius=0.05) for _ in range(cant_puntos)])
    for i, punto in enumerate(puntos):
        punto.move_to(i * puntos_separacion * RIGHT)
    puntos.shift(puntos_posicion)
    return(puntos)
    
def escenificar_lista(texto_original, corchete_color=WHITE, digitos_color=BLUE, cant_puntos = 18,chars_color=GREEN, comas_color=WHITE, font="Arial Black", font_size=36, puntos_posicion=2*UP,puntos_separacion=0.45,objetos_separacion=0.6, corchete2_pos = -1):
    # Extraer los elementos necesarios    
    corchete1 = texto_original[0]
    corchete2 = texto_original[-1]
    digitos = ''.join([char for char in texto_original if char.isdigit()])
    chars = ''.join([char for char in texto_original if char.isalpha()])
    comas = ''.join([char for char in texto_original if char in ","])

    # Crear objetos Text para cada elemento
    corchete1_objeto = Text(corchete1, font=font, font_size=font_size, color=corchete_color)
    corchete2_objeto = Text(corchete2, font=font, font_size=font_size, color=corchete_color)
    digitos_objeto = Text(digitos, font=font, font_size=font_size, color=digitos_color)
    chars_objeto = Text(digitos, font=font, font_size=font_size, color=chars_color)
    comas_objeto = Text(comas, font=font, font_size=font_size, color=comas_color)

    # Crear puntos
    puntos = crear_puntos(puntos_posicion, cant_puntos, puntos_separacion)
    for i, punto in enumerate(puntos):
        punto.move_to(i * puntos_separacion * RIGHT)
    puntos.shift(puntos_posicion)

    # Mover cada caracter del texto a cada uno de los puntos
    corchete1_objeto.move_to(puntos[0], aligned_edge=DOWN)
    corchete2_objeto.move_to(puntos[corchete2_pos], aligned_edge=DOWN)

    # Mover los dígitos a los primeros puntos pares
    for i, char in enumerate(digitos_objeto):
        if i * 2 + 1 < len(puntos):  # Verificar que hay suficientes puntos
            char.move_to(puntos[i * 2 + 1], aligned_edge=DOWN)

    # Mover las comas a los primeros puntos impares
    for i, char in enumerate(comas_objeto):
        if i * 2 < len(puntos):  # Verificar que hay suficientes puntos
            char.move_to(puntos[i * 2], aligned_edge=DOWN)
    comas_objeto.shift((objetos_separacion + 0.15) * RIGHT + 0.15 * DOWN)

    return VGroup(corchete1_objeto, digitos_objeto, comas_objeto, corchete2_objeto, puntos)

    
## Funciones libres del módulo # Creo que esta función está haciendo dos cosas
def crear_codigo(un_texto, movimiento):
    codigo = Code(code = un_texto, tab_width = 2.25, background = "window",language = "Python", font="Monospace").scale(0.8)
    codigo.move_to(movimiento)
    return codigo

def crear_terminal(un_texto):
    codigo = Code(code = un_texto, tab_width = 2.25, background = "window",language = "Python", font="Monospace").scale(0.8)
    codigo.move_to(movimiento)
    return codigo

def generar_snippet(self, mi_codigo):
    """Versión generador de crear_snippet"""
    for i in range(len(mi_codigo[2])):
        chars_por_seg = len(mi_codigo[2][i]) / 10
        # Animar otros objetos aquí, según sea necesario
        yield self.play(FadeIn(mi_codigo[1][i]))
        yield self.play(AddTextLetterByLetter(mi_codigo[2][i],   run_time=chars_por_seg, rate_func=linear))
    self.wait(1)

def avanzar_snippet(generador):
    for i in range(2):
        valor = next(generador) #  Obtener valores del generador, el primero es el número de fila, luego viene la línea
        # no hace falta la notación "self."" porque ya está hecho en el generador
        valor    

def construir_cuadro(self):                              
    # Crear rectángulos con la función crear_rectangulo
    tipos = crear_rectangulo(5, 0.8, "#15CFEA", 0.6, "Tipos de datos en python").move_to(UP * 3 + 0.19 * RIGHT)
    numeros = crear_rectangulo(2, 0.5, "#15CFEA", 0.7, "Numéricos").move_to(UP * 1.5 + LEFT * 5.125)
    enteros = crear_rectangulo(1.5, 0.5, YELLOW, 0.65, "Int").move_to(LEFT*6.25)
    flotantes = crear_rectangulo(1.5, 0.5, "#1ce364", 0.5, "Float").move_to(LEFT * 4)
    booleanos = crear_rectangulo(2, 0.5, "#AC1DB8", 0.85, "Booleanos").next_to(numeros.get_right() + RIGHT * 0.5)
    secuenciales = crear_rectangulo(2.25, 0.5, ORANGE, 0.65, "Secuenciales").next_to(booleanos.get_right() + RIGHT * 0.2)
    listas = crear_rectangulo(1.75, 0.5, PINK, 0.65, "Listas").move_to(ORIGIN + 1.45 * DOWN + RIGHT * 0.2)
    cadena = crear_rectangulo(1.75, 0.5, "#DA1884", 0.8, "String").next_to(listas.get_left() + LEFT * 2.25)
    tuplas = crear_rectangulo(1.5, 0.5, MAROON, 0.75, "Tuplas").next_to(listas.get_right()+ RIGHT * 0.175)
    set = crear_rectangulo(1.75, 0.5, "#05FFA6", 0.65, "Conjunto").next_to(secuenciales.get_right() + RIGHT * 0.5)
    diccionario = crear_rectangulo(2, 0.5, GOLD, 0.85, "Diccionario").next_to(set.get_right() + RIGHT * 0.5)


    #punto_medio = (tipos.get_bottom() - secuenciales.get_top()/2)[1]
    punto = Point(UP * (secuenciales.get_top() + 0.425)).set_color(WHITE)
    codo1 = crear_codo(numeros.get_top(), punto.get_center())
    codo2 = crear_codo(diccionario.get_top(), punto.get_center())
    codo3 = crear_codo(numeros.get_bottom(), enteros.get_right())
    linea1 = Line(tipos.get_bottom(), secuenciales.get_top())
    linea2 = Line(booleanos.get_top(), booleanos.get_top() + 0.425 * UP)
    linea3 = Line(set.get_top(), set.get_top() + 0.425 * UP)
    linea4 = Line(enteros.get_right(), flotantes.get_left())
    linea5 = Line(numeros.get_bottom(), get_nearest_point(linea4.start, linea4.end, numeros.get_bottom()))
    linea6 = Line(secuenciales.get_bottom(), listas.get_top())
        
    punto2 = Point(listas.get_top() + UP * 0.45)
    codo4 = crear_codo(cadena.get_top(), punto2.get_center())
    codo5 = crear_codo(tuplas.get_top(), punto2.get_center())
    self.add(tipos, numeros, flotantes, enteros, booleanos, secuenciales, set, diccionario, codo1, codo2,
    linea1, linea2, linea3, linea4, linea5, linea6, cadena, listas, tuplas, codo4, codo5)