from manim import *
import math
from manim.utils.color import RED, YELLOW_B, BLUE, WHITE, BLACK, RED_B

def crear_etiqueta(x, nivel, width=3.25, height=0.6):
    """Crea una etiqueta gráfica con texto que indica el número de electrones en un nivel.
    
    Args:
        x (int): Número de electrones a mostrar en la etiqueta.
        nivel (int/str): Nivel de energía al que pertenecen los electrones.
        width (float, optional): Ancho del fondo de la etiqueta. Default 3.25.
        height (float, optional): Alto del fondo de la etiqueta. Default 0.6.
    
    Returns:
        VGroup: Grupo de manim que contiene el fondo (RoundedRectangle) y el texto,
               centrados y listos para mostrar.
    """
    if x == 1:
        texto = Text(f"{x} electrón en nivel {nivel}", font="Liberation Sans", font_size=42, weight=BOLD , color=BLACK).scale(0.45)
    else:
        texto = Text(f"{x} electrones en nivel {nivel}", font="Liberation Sans", font_size=42, weight=BOLD , color=BLACK).scale(0.45)
    fondo = RoundedRectangle(corner_radius=0.2, width=width, height=height, color=BLACK, fill_color=WHITE, fill_opacity=1)
    etiqueta = VGroup(fondo, texto)
    texto.move_to(fondo.get_center())
    return etiqueta


def crear_circulo_sombreado(
    radio=1,
    color=RED_B,
    opacidad_relleno=0.8,
    sheen=0.5,
    stroke_color=WHITE,
    stroke_width=1,
    stroke_opacidad=0
):
    """Crea un círculo con efectos visuales personalizables.
    
    Args:
        radio (float, optional): Radio del círculo. Default 1.
        color (str, optional): Color de relleno (manim color). Default RED_B.
        opacidad_relleno (float, optional): Opacidad del relleno (0-1). Default 0.8.
        sheen (float, optional): Intensidad del efecto brillo. Default 0.5.
        stroke_color (str, optional): Color del borde. Default WHITE.
        stroke_width (int, optional): Grosor del borde. Default 1.
        stroke_opacidad (int, optional): Opacidad del borde (0-1). Default 0.
    
    Returns:
        Circle: Objeto Circle de manim con los efectos aplicados.
    """
    circulo = Circle(radius=radio)
    circulo.set_fill(color=color, opacity=opacidad_relleno)
    circulo.set_sheen(sheen)
    circulo.set_stroke(color=stroke_color, width=stroke_width, opacity=stroke_opacidad)
    return circulo


def crear_icono_alerta():
    """Genera un icono de alerta (triángulo con signo de exclamación).
    
    El icono consiste en:
    - Un triángulo rojo con borde
    - Un triángulo ligeramente más pequeño superpuesto
    - Un signo '!' amarillo en el centro
    
    Returns:
        VGroup: Grupo que contiene todos los elementos del icono de alerta.
    """
    # Triángulo equilátero como base
    triangulo = Triangle()
    triangulo.set_stroke(RED, width=4)
    triangulo.scale(1.25)

    triangulo2 = triangulo.copy().scale(0.9).shift(0.04*DOWN)

    # Signo de exclamación
    signo = Text("!", font_size=90, color=YELLOW_B)
    signo.move_to(triangulo.get_center() + 0.15 * DOWN)

    # Agrupar todo
    simbolo_alerta = VGroup(triangulo, triangulo2 ,signo)

    return simbolo_alerta


def crear_liston_hexagonal():
    """Crea un listón compuesto por hexágonos regulares rotados.
    
    Crea un hexágono base y lo transforma (rota 30° y escala) para usarlo como patrón.
    Nota: La función actualmente solo define los puntos base pero no retorna nada visible.
    
    Returns:
        None: Actualmente no retorna ningún objeto visual (requiere implementación adicional).
    """
    # Puntos del hexágono regular (antes de rotación y escala)
    puntos = [
        UP * 2,
        UP * 1 + RIGHT * math.sqrt(3),
        DOWN * 1 + RIGHT * math.sqrt(3),
        DOWN * 2,
        DOWN * 1 + LEFT * math.sqrt(3),
        UP * 1 + LEFT * math.sqrt(3),
    ]

    # Función auxiliar para crear hexágonos ya transformados
    def crear_hexagono(color, desplazamiento):
        return Polygon(*puntos,
                       fill_color=color,
                       fill_opacity=1,
                       stroke_opacity=0
               ).rotate(30*DEGREES).scale(0.4).shift(desplazamiento)
    

def crear_circunferencias(n: int, centro=ORIGIN, radio_inicial: float = 0.55, paso: float = 0.3, color=BLUE) -> list:
    """Genera una serie de circunferencias concéntricas con radios incrementales.
    
    Crea 'n' círculos concéntricos alrededor de un punto central, donde cada círculo
    tiene un radio mayor que el anterior según el paso especificado.

    Args:
        n (int): Número de circunferencias a crear.
        centro (np.array, optional): Punto central de las circunferencias. 
            Default ORIGIN (0,0,0).
        radio_inicial (float, optional): Radio de la primera circunferencia. 
            Default 0.55.
        paso (float, optional): Incremento del radio para cada circunferencia. 
            Default 0.3.
        color (str, optional): Color de las circunferencias (color manim). 
            Default BLUE.

    Returns:
        list: Lista de objetos Circle de manim, ordenados de menor a mayor radio.
    """
    return [
        Circle(radius=radio_inicial + i * paso, color=color, stroke_width=2, fill_opacity=0).move_to(centro)
        for i in range(n)
    ]


def ubicar_objeto_en_circunferencia(n: int, radio: float, centro=ORIGIN, color=WHITE) -> VGroup:
    """Distribuye objetos circulares uniformemente sobre una circunferencia imaginaria.
    
    Crea 'n' pequeños círculos distribuidos equitativamente alrededor de una 
    circunferencia de radio dado, comenzando desde la posición superior (90 grados).

    Args:
        n (int): Número de objetos a distribuir en la circunferencia.
        radio (float): Radio de la circunferencia donde se ubicarán los objetos.
        centro (np.array, optional): Centro de la circunferencia. Default ORIGIN.
        color (str, optional): Color de los objetos (color manim). Default WHITE.

    Returns:
        VGroup: Grupo manim que contiene todos los objetos circulares distribuidos.
               Cada objeto es un círculo pequeño con relleno semitransparente.
    """
    return VGroup(*[
        Circle(radius=0.08, color=color, fill_opacity=0.6, fill_color=color)
        .move_to(centro + radio * np.array([np.cos(theta + PI/2), np.sin(theta + PI/2), 0]))
        for theta in np.linspace(0, TAU, n, endpoint=False)
    ])


def distribuir_objetos_en_circunferencia(
    objeto: type = Circle,
    n: int = 1,
    radio: float = 1.0,
    centro: np.ndarray = ORIGIN,
    angulo_inicial: float = PI/2,
    **kwargs
) -> VGroup:
    """Distribuye objetos de Manim uniformemente alrededor de una circunferencia.
    
    Args:
        objeto (type, optional): Clase del objeto Manim a distribuir (Circle, Square, Dot, etc).
            Default Circle.
        n (int, optional): Número de objetos a distribuir. Default 1.
        radio (float, optional): Radio de la circunferencia de distribución. Default 1.0.
        centro (np.ndarray, optional): Centro de la circunferencia. Default ORIGIN.
        angulo_inicial (float, optional): Ángulo inicial en radianes (0=este, π/2=norte). Default π/2.
        **kwargs: Argumentos adicionales para pasar al constructor del objeto (color, radius, etc).

    Returns:
        VGroup: Grupo que contiene todos los objetos distribuidos.

    Examples:
        # Círculos rojos
        distribuir_objetos_en_circunferencia(
            objeto=Circle,
            n=5,
            radio=2,
            color=RED,
            radius=0.1,
            fill_opacity=0.8
        )

        # Estrellas verdes
        distribuir_objetos_en_circunferencia(
            objeto=Star,
            n=7,
            color=GREEN,
            outer_radius=0.2
        )
    """
    if 'radius' not in kwargs and objeto == Circle:
        kwargs.setdefault('radius', 0.08)  # Valor por defecto solo para Circle
    
    objetos = []
    for theta in np.linspace(0, TAU, n, endpoint=False):
        pos = centro + radio * np.array([np.cos(theta + angulo_inicial), 
                                       np.sin(theta + angulo_inicial), 
                                       0])
        new_obj = objeto(**kwargs).move_to(pos)
        objetos.append(new_obj)
    
    return VGroup(*objetos)