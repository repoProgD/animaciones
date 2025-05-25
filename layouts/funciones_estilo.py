from manim import *

def alinear_horizontal(grupo, x=0, animado=False):
    """
    Alinea horizontalmente los objetos en un grupo dado, manteniendo su coordenada y.
    (Es decir, los alinea en la misma columna vertical)

    Parámetros:
    - grupo: VGroup o Group de objetos de Manim
    - x: coordenada x deseada
    - animado: si True, devuelve animaciones en lugar de mover directamente

    Retorna:
    - Lista de animaciones si animado=True
    - None si animado=False
    """
    # Creamos un vector de posición [x, y, z] donde:
    # - x es la nueva coordenada horizontal deseada,
    # - obj.get_y() conserva la altura actual del objeto,
    # - obj.get_z() conserva la profundidad (útil en escenas 3D).

    if animado:
        return [obj.animate.move_to([x, obj.get_y(), obj.get_z()]) for obj in grupo]
    else:
        for obj in grupo:
            obj.move_to([x, obj.get_y(), obj.get_z()])


def alinear_vertical(grupo, y=0, animado=False):
    """
    Alinea verticalmente los objetos en un grupo dado, manteniendo su coordenada x.

    Parámetros:
    - grupo: VGroup o Group de objetos de Manim
    - y: coordenada y deseada
    - animado: si True, devuelve animaciones en lugar de mover directamente

    Retorna:
    - Lista de animaciones si animado=True
    - None si animado=False
    """

    # Creamos un vector de posición [x, y, z] donde:
    # - obj.get_x() conserva la coordenada x actual del objeto,
    # - y es la nueva coordenada vertical deseada,
    # - obj.get_z() conserva la profundidad (útil en escenas 3D).

    if animado:
        return [obj.animate.move_to([obj.get_x(), y, obj.get_z()]) for obj in grupo]
    else:
        for obj in grupo:
            obj.move_to([obj.get_x(), y, obj.get_z()])



def centrar_en(objeto, objetivo, direccion="x", animado=False):
    """
    Centra un objeto con respecto a otro en la dirección indicada ('x' o 'y').

    Parámetros:
    - objeto: objeto que se va a mover
    - objetivo: objeto con respecto al cual se centra
    - direccion: 'x' o 'y'
    - animado: si True, devuelve una animación

    Retorna:
    - Una animación si animado=True
    - None si animado=False
    """
    pos = objeto.get_center()
    objetivo_pos = objetivo.get_center()

    if direccion == "x":
        nueva_pos = [objetivo_pos[0], pos[1], pos[2]]
    elif direccion == "y":
        nueva_pos = [pos[0], objetivo_pos[1], pos[2]]
    else:
        raise ValueError("Dirección debe ser 'x' o 'y'")

    if animado:
        return objeto.animate.move_to(nueva_pos)
    else:
        objeto.move_to(nueva_pos)

def distribuir_horizontal(grupo, espacio=1.0, animado=False):
    """
    Distribuye objetos horizontalmente con espacio constante entre sus centros.

    Parámetros:
    - grupo: lista o VGroup
    - espacio: distancia entre centros
    - animado: si True, devuelve animaciones

    Retorna:
    - Lista de animaciones si animado=True
    - None si animado=False
    """
    x_actual = 0
    total_ancho = sum(obj.width for obj in grupo) + espacio * (len(grupo) - 1)
    x_inicial = -total_ancho / 2

    animaciones = []
    for obj in grupo:
        destino_x = x_inicial + obj.width / 2
        nueva_pos = [destino_x, obj.get_y(), obj.get_z()]
        if animado:
            animaciones.append(obj.animate.move_to(nueva_pos))
        else:
            obj.move_to(nueva_pos)
        x_inicial = destino_x + obj.width / 2 + espacio

    return animaciones if animado else None


def ajustar_texto_a_contenedor(texto: Text, contenedor: Mobject, padding: float = 0.1):
    """
    Escala el texto para que quepa dentro del contenedor.

    Parámetros:
        texto: objeto Text
        contenedor: Mobject contenedor (por ejemplo, un Rectangle o Square)
        padding: margen opcional (en unidades de Manim)

    Devuelve:
        texto escalado (modificado in-place)
    """
    ancho_disp = contenedor.width - 2 * padding
    alto_disp = contenedor.height - 2 * padding

    escala_horizontal = ancho_disp / texto.width
    escala_vertical = alto_disp / texto.height

    escala_final = min(escala_horizontal, escala_vertical)
    texto.scale(escala_final)

    return texto


def desdoblar_texto(texto: Text, distancia=2):
    """
    Coloca un texto y luego las desplaza:
    - Letras con índice par: hacia arriba
    - Letras con índice impar: hacia abajo

    Parámetros:
    - texto: objeto Text
    - distancia: cantidad de unidades a desplazar (default: 2)

    Devuelve:
    - Una lista de animaciones de movimiento
    """
    letras = texto.submobjects

    # Crear las animaciones de desplazamiento
    animaciones = []
    for i, letra in enumerate(letras):
        desplazamiento = distancia * UP if i % 2 == 0 else distancia * DOWN
        animaciones.append(letra.animate.shift(desplazamiento))

    return animaciones


def rebotar(objeto, altura=1, duracion=1):
    """
    Devuelve una animación que hace rebotar el objeto.

    Parámetros:
    - objeto: VMobject al que se le aplica el rebote.
    - altura: altura máxima del rebote (en unidades de Manim).
    - duracion: duración total del rebote.

    Retorna:
    - Una Animation que puede usarse en scene.play().
    """
    def rebote_alpha(t):
        # Función tipo ease-out-bounce aproximada
        if t < 0.3636:
            return 7.5625 * t * t
        elif t < 0.7272:
            t -= 0.5454
            return 7.5625 * t * t + 0.75
        elif t < 0.9090:
            t -= 0.8181
            return 7.5625 * t * t + 0.9375
        else:
            t -= 0.9545
            return 7.5625 * t * t + 0.984375

    def rebote_fn(mob, alpha):
        desplazamiento = altura * (1 - rebote_alpha(alpha))
        mob.move_to(objeto.get_center() + desplazamiento * UP)

    return AnimationGroup(
        ApplyFunction(lambda m: m.move_to(objeto.get_center()), objeto),
        UpdateFromAlphaFunc(objeto, rebote_fn, run_time=duracion, rate_func=linear),
    )


def rebote_horizontal_bounce(objeto, desplazamiento=3, duracion=1):
    """
    Devuelve una animación que mueve un objeto horizontalmente con efecto de rebote.

    Parámetros:
    - objeto: Mobject al que se le aplica el rebote.
    - desplazamiento: cuánto se mueve en X antes de rebotar.
    - duracion: duración total de la animación.

    Retorna:
    - Una Animation usable en scene.play().
    """
    def rebote_alpha(t):
        # Ease-out bounce (como en el eje Y original)
        if t < 0.3636:
            return 7.5625 * t * t
        elif t < 0.7272:
            t -= 0.5454
            return 7.5625 * t * t + 0.75
        elif t < 0.9090:
            t -= 0.8181
            return 7.5625 * t * t + 0.9375
        else:
            t -= 0.9545
            return 7.5625 * t * t + 0.984375

    x_inicial = objeto.get_center()[0]

    def rebote_fn(mob, alpha):
        desplazamiento_actual = desplazamiento * rebote_alpha(alpha)
        nueva_posicion = np.array([
            x_inicial + desplazamiento_actual,
            mob.get_y(),
            0
        ])
        mob.move_to(nueva_posicion)

    return UpdateFromAlphaFunc(objeto, rebote_fn, run_time=duracion, rate_func=linear)