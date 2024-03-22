from manim import *
import herramientas as h
    
def construir_cuadro(self):                              
    # Crear rectángulos con la función crear_rectangulo
    tipos = h.crear_rectangulo(4, 0.8, "#15CFEA", 0.6, "Tipos de datos en python").move_to(UP * 3)
    numeros = h.crear_rectangulo(1.75, 0.5, "#15CFEA", 0.7, "Numéricos").move_to(UP * 1.5 + LEFT * 5.125)
    enteros = h.crear_rectangulo(1.5, 0.5, YELLOW, 0.65, "Int").move_to(LEFT*6.25)
    flotantes = h.crear_rectangulo(1.5, 0.5, "#1ce364", 0.5, "Float").move_to(LEFT * 4)
    booleanos = h.crear_rectangulo(1.75, 0.5, "#AC1DB8", 0.85, "Booleanos").next_to(numeros.get_right() + RIGHT * 0.5)
    secuenciales = h.crear_rectangulo(2, 0.5, ORANGE, 0.65, "Secuenciales").next_to(booleanos.get_right() + RIGHT * 0.5)
    listas = h.crear_rectangulo(1.75, 0.5, PINK, 0.65, "Listas").move_to(ORIGIN + 1.45 * DOWN)
    cadena = h.crear_rectangulo(1.75, 0.5, "#DA1884", 0.8, "String").next_to(listas.get_left() + LEFT * 2.75)
    tuplas = h.crear_rectangulo(1.5, 0.5, MAROON, 0.75, "Tuplas").next_to(listas.get_right()+ RIGHT * 0.5)
    set = h.crear_rectangulo(1.75, 0.5, "#05FFA6", 0.65, "Conjunto").next_to(secuenciales.get_right() + RIGHT * 0.5)
    diccionario = h.crear_rectangulo(2, 0.5, GOLD, 0.85, "Diccionario").next_to(set.get_right() + RIGHT * 0.5)

    #punto_medio = (tipos.get_bottom() - secuenciales.get_top()/2)[1]
    punto = Point(UP * (secuenciales.get_top() + 0.425)).set_color(WHITE)
    codo1 = h.crear_codo(numeros.get_top(), punto.get_center())
    codo2 = h.crear_codo(diccionario.get_top(), punto.get_center())
    codo3 = h.crear_codo(numeros.get_bottom(), enteros.get_right())
    linea1 = Line(tipos.get_bottom(), secuenciales.get_top())
    linea2 = Line(booleanos.get_top(), booleanos.get_top() + 0.425 * UP)
    linea3 = Line(set.get_top(), set.get_top() + 0.425 * UP)
    linea4 = Line(enteros.get_right(), flotantes.get_left())
    linea5 = Line(numeros.get_bottom(), h.get_nearest_point(linea4.start, linea4.end, numeros.get_bottom()))
    linea6 = Line(secuenciales.get_bottom(), listas.get_top())
        
    punto2 = Point(listas.get_top() + UP * 0.45)
    codo4 = h.crear_codo(cadena.get_top(), punto2.get_center())
    codo5 = h.crear_codo(tuplas.get_top(), punto2.get_center())
    self.add(tipos, numeros, flotantes, enteros, booleanos, secuenciales, set, diccionario, codo1, codo2,
    linea1, linea2, linea3, linea4, linea5, linea6, cadena, listas, tuplas, codo4, codo5)
    