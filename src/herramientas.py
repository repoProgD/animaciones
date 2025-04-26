from manim import *
from pathlib import Path

# Ruta base de imágenes
IMAGES_PATH = Path(__file__).resolve().parent.parent / "images"

# Caché interno de imágenes ya cargadas
_imagen_cache = {}

#### funciones

def cargar_imagen(nombre_archivo, **kwargs):
    """
    Carga una imagen desde la carpeta 'images' y la devuelve como ImageMobject.
    Usa cache para no cargar varias veces la misma imagen.

    Parámetros:
    - nombre_archivo: str, nombre del archivo (ej. 'logorobo.png')
    - kwargs: parámetros opcionales que quieras pasar a ImageMobject.

    Retorna:
    - Un ImageMobject listo para usar (nueva instancia cada vez para que puedas moverlas independientes).
    """
    ruta_imagen = IMAGES_PATH / nombre_archivo
    if not ruta_imagen.exists():
        raise FileNotFoundError(f"No se encontró la imagen: {ruta_imagen}")

    # Si ya está en el cache, usamos el archivo ya cargado
    if nombre_archivo not in _imagen_cache:
        _imagen_cache[nombre_archivo] = str(ruta_imagen)

    # Cada vez que llamás, devolvemos un nuevo ImageMobject para que puedas manipularlo independiente
    return ImageMobject(_imagen_cache[nombre_archivo], **kwargs)


def cargar_imagenes_desde_carpeta(nombre_carpeta, tipo="imagen", **kwargs):
    """
    Carga archivos desde una subcarpeta como imágenes rasterizadas (PNG/JPG) o vectores SVG.

    Parámetros:
    - nombre_carpeta: nombre de la subcarpeta dentro de 'images'
    - tipo: 'imagen' para PNG/JPG, 'vector' para SVG
    - kwargs: parámetros opcionales que se pasan a ImageMobject o SVGMobject

    Retorna:
    - Group (para imágenes) o VGroup (para vectores)
    """
    ruta_carpeta = IMAGES_PATH / nombre_carpeta

    if not ruta_carpeta.exists() or not ruta_carpeta.is_dir():
        raise FileNotFoundError(f"No se encontró la carpeta: {ruta_carpeta}")

    archivos = sorted(ruta_carpeta.glob("*"))

    objetos = []

    for archivo in archivos:
        if tipo == "imagen":
            if archivo.suffix.lower() not in [".png", ".jpg", ".jpeg"]:
                continue  # Salteamos si no es una imagen raster

            # Cacheamos la ruta
            if archivo.name not in _imagen_cache:
                _imagen_cache[archivo.name] = str(archivo)

            obj = ImageMobject(_imagen_cache[archivo.name], **kwargs)
            objetos.append(obj)

        elif tipo == "vector":
            if archivo.suffix.lower() != ".svg":
                continue  # Salteamos si no es SVG

            obj = SVGMobject(str(archivo), **kwargs)
            objetos.append(obj)

        else:
            raise ValueError(f"Tipo desconocido: {tipo}. Usa 'imagen' o 'vector'.")

    if tipo == "imagen":
        return Group(*objetos)
    elif tipo == "vector":
        return VGroup(*objetos)

    # No debería llegar acá
    return None


def posicionar_logo_h(self, logo):
    """
    Posiciona un logo en la escena con una posición específica y opacidad,
    y lo agrega a la escena.

    Parámetros:
    - self: El contexto de la escena en Manim.
    - logo: El ImageMobject que se desea posicionar.
    """
    logo.move_to(DOWN * 2.8 + LEFT * 5.9).set_opacity(0.55)
    self.add(logo)



def toggle_grilla(escena, mostrar=True):
    if mostrar:
        grilla = GrillaVertical()
        escena.add(grilla)



def crear_anchors(group):
    """
    Crea un Group de Point() ubicados en el centro de cada subobjeto del Group dado.

    Parámetros:
    - group: Group o VGroup de Manim.

    Retorna:
    - Group de Point()s ubicados en los centros de los subobjetos.
    """
    return Group(*[Point(mobj.get_center()) for mobj in group])


#### Clases
class Logo(Group):
    def __init__(self, **kwargs):
        # inicializar el VMobject
        super().__init__(**kwargs)
        logo_ruta = Path(__file__).resolve().parent.parent / "images" / "logorobo.png"  # Manim siempre buscará imágenes relativas al archivo de la animación 
                                                                                        # actual, por eso hay que pasarle un Path absoluto.
        logo = ImageMobject(str(logo_ruta)).scale(0.65)
        logo.move_to(DOWN * 2.8 + LEFT * 5.9).set_opacity(0.55)   
        self.add(logo)

class LogoV(Group):  # Group permite ImageMobject y otros tipos mixtos
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logo = ImageMobject("../images/logorobo.png").scale(0.55)
        logo.move_to([-2.94, -6.15, 0]).set_opacity(0.55)
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


class GrillaVertical(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Crear una rejilla 9:16 (orientación vertical)
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1],    # Ancho: 9 unidades
            y_range=[-8, 8, 1],        # Alto: 16 unidades
            x_length=9,
            y_length=16,
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 1
            }
        )

        self.add(grid)










####################################  ##################################



