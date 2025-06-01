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

##########################################################################################

def alinear_vertical(grupo, y=0, animado=False):
    """
    Alinea verticalmente los objetos(por su centro) en un grupo dado, 
    manteniendo su coordenada x.
    (Es decir, los alinea en la misma fila horizontal)
    IMPORTANTE: No sirve para texto.

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

############################## alinear texto verticalmente ################################

def get_baseline_offset_to(y_objetivo, texto, font_size_ref=120):
    """
    Devuelve el desplazamiento necesario para alinear la baseline de `texto` a `y_objetivo`.
    Si tenés problema con una fuente grande, podés usar font_size = 60-80 y escalá después.
    """
    palabra = texto.text
    font_size = texto.font_size

    # Calcular baseline relativa usando una 'x' como referencia
    texto_x = Text("x", font_size=font_size_ref)
    texto_mix = Text(palabra + "x", font_size=font_size_ref)
    bottom_x_sola = texto_x.get_bottom()[1]
    bottom_x_en_mix = texto_mix.submobjects[-1].get_bottom()[1]
    correccion = bottom_x_en_mix - bottom_x_sola  
    escala = font_size / font_size_ref
    correccion_escalada = correccion * escala # Acá ya tenemos el movimiento que necesitan para equipararse ahora queda sumar la distancia al y_objetivo
    
    return y_objetivo - correccion_escalada


def alinear_texto_verticalmente(grupo, y=0, animado=False, duracion=1.5):
    """
    Alinea por baseline verticalmente a y, manteniendo x de cada objeto.
    """
    animaciones = []
    for texto in grupo:
        y_ajustado = get_baseline_offset_to(y, texto)
        
        if animado:
            animaciones.append(texto.animate.move_to([texto.get_x(), y_ajustado, texto.get_z()]))
        else:
            texto.move_to([texto.get_x(), y_ajustado, texto.get_z()])
       
    if animado:
        return animaciones

#class AlinearTextoVerticalmente(Scene):
#    def construct(self):
#        t1 = Text("Uno", font="Liberation Sans", font_size=80).move_to([-5, 2, 0])
#        t1_5 = Text("queso", font="Liberation Sans", font_size=80).move_to([-2.35, 1, 0])
#        t2 = Text("Dos", font="Liberation Sans", font_size=80).move_to([0, -1, 0])
#        t3 = Text("gato1", font="Liberation Sans", font_size=80).move_to([3, -5, 0])
#        grupo = VGroup(t1, t1_5, t2, t3)
#        self.add(grupo)
#        self.wait(1)

#        # Línea base de referencia
#        y = -2
#        linea = Line(7 * LEFT, 7 * RIGHT, color=YELLOW).shift(2.35*DOWN)
#        self.add(linea)

#        # Animar alineación por baseline
#        anims = alinear_texto_verticalmente(grupo, y=y, animado=True)
#        self.play(*anims)
#        self.wait()


#############################################################################

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

#############################################################################

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

############################################################################

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

###########################################################################

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

###########################################################################

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

########################################################################

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

#############################################################################

def get_baseline_correction(texto_str, font_size=60):
    """Devuelve cuánto hay que subir o bajar `texto_str` para alinear su baseline con la de una 'x' suelta."""
    font_size_para_calculo = 120
    texto_x = Text("x", font_size=font_size_para_calculo)
    texto_mix = Text(texto_str + "x", font_size=font_size_para_calculo)

    bottom_x_sola = texto_x.get_bottom()[1]
    bottom_x_en_mix = texto_mix.submobjects[-1].get_bottom()[1]

    correccion = bottom_x_en_mix - bottom_x_sola
    escala = font_size / font_size_para_calculo
    return correccion * escala

def alinear_por_baseline(textos, animacion=False, duracion=1.5, scene=None):
    """Corrige verticalmente para alinear la baseline de los textos.
    Si `animacion=True`, requiere que pases `scene` para ejecutar la animación.
    alinear_por_baseline(textos, animacion=True, scene=self)
    """
    animaciones = []
    for texto in textos:
        palabra = texto.text
        font_size = texto.font_size
        correccion = get_baseline_correction(palabra, font_size=font_size)

        if animacion:
            animaciones.append(texto.animate.shift(DOWN * correccion))
        else:
            texto.shift(DOWN * correccion)

    if animacion and scene is not None:
        scene.play(*animaciones, run_time=duracion)

#############################################################################

def resaltar_palabras(texto, indices, color=YELLOW, font_size=48, **kwargs):
    """
    Convierte un texto en una lista de objetos Text, resaltando ciertas palabras por índice.

    Cada palabra del texto es transformada en un objeto `Text` de Manim. Las palabras en las 
    posiciones indicadas por `indices` se colorean con el color especificado.

    Requiere llamar a alinear_por_baseline(grupo) después de usar esta función.
    No usar alinear_por_baseline() antes de usar arrange() en VGroup.

    Parameters
    ----------
    texto : str
        La cadena de texto a procesar.
    indices : list of int
        Índices (basados en espacios) de las palabras que se desean resaltar.
    color : Manim Color, optional
        Color para las palabras resaltadas (por defecto es YELLOW).
    font_size : int, optional
        Tamaño de fuente para todos los objetos Text (por defecto es 48).
    **kwargs : dict
        Argumentos adicionales que se pasan a cada objeto `Text`.

    Returns
    -------
    list of Text
        Lista de objetos `Text` correspondientes a cada palabra del texto original,
        con las palabras resaltadas según `indices`.
    """
    palabras = texto.split()
    lista_textos = []

    for i, palabra in enumerate(palabras):
        txt = Text(palabra, font_size=font_size, **kwargs)
        if i in indices:
            txt.set_color(color)
        lista_textos.append(txt)

    return lista_textos

#################################################################

    def escribir_a_maquina(scene, texto, duracion=2, font_size=48, **kwargs):
    """
    Muestra el texto letra por letra, como una máquina de escribir.
    En principio, no se diferencia demasiado de la clase AddTextLetterByLetter
    de manim pero permite mayor personalización, por ejemplo con sonidos
    o escucha de eventos. Usar cuando necesite mayor control o personalización.

    Parámetros:
    - scene: instancia de Scene
    - texto: string a mostrar
    - duracion: duración total de la animación
    - font_size: tamaño de fuente
    - kwargs: otros parámetros para `Text`
    """
    texto_mobj = Text(texto, font_size=font_size, **kwargs)
    texto_mobj.set_opacity(0)  # Ocultamos todo inicialmente
    scene.add(texto_mobj)

    letras = texto_mobj.submobjects
    tiempo_por_letra = duracion / len(letras)

    for letra in letras:
        scene.play(letra.animate.set_opacity(1), run_time=tiempo_por_letra)


###############################justificar#################################

def dividir_equilibradamente(texto, num_lineas):
    """
    Divide un texto en un número dado de líneas intentando balancear la cantidad de caracteres
    en cada línea para que sean lo más parecidas posible en longitud.

    Args:
        texto (str): Texto original a dividir.
        num_lineas (int): Cantidad de líneas en que se quiere dividir el texto.

    Returns:
        list[str]: Lista con las líneas resultantes, cada una como un string.
    """
    palabras = texto.split()
    total_chars = sum(len(p) for p in palabras) + len(palabras) - 1  # Cuenta espacios entre palabras
    target_chars = total_chars / num_lineas

    lineas = [[] for _ in range(num_lineas)]
    longitudes = [0] * num_lineas

    for palabra in palabras:
        # Elegir la línea con menor cantidad de caracteres actuales para añadir la palabra
        mejor_opcion = min(
            range(num_lineas),
            key=lambda i: (longitudes[i], i)
        )
        # Si ya hay palabras en la línea, sumar un espacio extra para separación
        if lineas[mejor_opcion]:
            longitudes[mejor_opcion] += 1  # espacio entre palabras
        lineas[mejor_opcion].append(palabra)
        longitudes[mejor_opcion] += len(palabra)

    return [" ".join(linea) for linea in lineas]


def longitud_maxima_linea(lineas):
    """
    Calcula la longitud máxima en caracteres de una lista de líneas de texto.

    Args:
        lineas (list[str]): Lista de líneas de texto.

    Returns:
        int: La longitud máxima entre todas las líneas.
    """
    return max(len(linea) for linea in lineas)


def justificar_lineas_con_espacios(lineas, largo_objetivo):
    """
    Justifica cada línea agregando underscores como espacios para que todas tengan la misma longitud objetivo.
    Si la línea tiene una sola palabra, se agregan underscores al final para igualar la longitud.

    Args:
        lineas (list[str]): Líneas originales sin justificar.
        largo_objetivo (int): Largo que debe tener cada línea justificada.

    Returns:
        list[str]: Líneas justificadas con underscores en lugar de espacios para controlar el espacio visual.
    """
    lineas_justificadas = []

    for linea in lineas:
        palabras = linea.split(" ")
        if len(palabras) == 1:
            # No se puede justificar una sola palabra con espacios entre palabras
            palabra_unica = palabras[0]
            faltantes = largo_objetivo - len(palabra_unica)
            if faltantes > 0:
                # Rellenar con underscores para alcanzar el largo deseado
                palabra_unica += "_" * faltantes
            lineas_justificadas.append(palabra_unica)
            continue

        # Unir palabras sin espacios para calcular el espacio necesario a distribuir
        linea_sin_espacios = "".join(palabras)
        largo_actual = len(linea_sin_espacios)
        espacios_necesarios = largo_objetivo - largo_actual

        if espacios_necesarios <= 0:
            # La línea ya es igual o más larga que el objetivo, no se añade espacios extra
            lineas_justificadas.append(linea_sin_espacios)
            continue

        cantidad_espacios = len(palabras) - 1
        espacios_base = espacios_necesarios // cantidad_espacios
        espacios_extra = espacios_necesarios % cantidad_espacios

        linea_justificada = ""
        for i, palabra in enumerate(palabras):
            linea_justificada += palabra
            if i < cantidad_espacios:
                # Distribuir los espacios extra entre los primeros espacios
                extra = 1 if i < espacios_extra else 0
                # Si queda un carácter faltante no repartido, agregar underscore extra al principio
                if i == 0 and espacios_extra == 0 and espacios_base * cantidad_espacios < espacios_necesarios:
                    linea_justificada += "_"
                linea_justificada += "_" * (espacios_base + extra)

        lineas_justificadas.append(linea_justificada)

    return lineas_justificadas


def indices_guiones_bajos(texto):
    """
    Obtiene los índices donde aparecen los caracteres underscore '_' en un texto.

    Args:
        texto (str): Texto a analizar.

    Returns:
        list[int]: Lista con los índices de cada underscore en el texto.
    """
    return [i for i, c in enumerate(texto) if c == "_"]

############################### fin de justificar ############################
###31/05/25#################### demo_tipo_maquina#############################
def escribir_a_maquina(scene, texto, duracion=2, font_size=48, **kwargs):
    """
    Muestra el texto letra por letra, como una máquina de escribir.
    En principio, no se diferencia demasiado de la clase AddTextLetterByLetter
    de manim pero permite mayor personalización, por ejemplo con sonidos
    o escucha de eventos. Usar cuando necesite mayor control o personalización.

    Parámetros:
    - scene: instancia de Scene
    - texto: string a mostrar
    - duracion: duración total de la animación
    - font_size: tamaño de fuente
    - kwargs: otros parámetros para `Text`
    """
    texto_mobj = Text(texto, font_size=font_size, **kwargs)
    texto_mobj.set_opacity(0)  # Ocultamos todo inicialmente
    scene.add(texto_mobj)

    letras = texto_mobj.submobjects
    tiempo_por_letra = duracion / len(letras)

    for letra in letras:
        scene.play(letra.animate.set_opacity(1), run_time=tiempo_por_letra)

############################## cambio de colores #################################
def cambio_color_letra_a_letra(scene, texto, colores, font_size=48, duracion_total=2, **kwargs):
    """
    Cambia el color de cada letra de un texto una por una, de forma animada.

    Parámetros:
    - scene: instancia de `Scene` en la que se reproducirá la animación.
    - texto: string que se mostrará letra por letra.
    - colores: lista de colores (uno por letra o menos — los faltantes no cambian).
    - font_size: tamaño de la fuente para el texto (por defecto 48).
    - duracion_total: duración total de la animación (por defecto 2 segundos).
    - kwargs: otros argumentos opcionales para el objeto `Text`.

    Ejemplo de uso:
        cambio_color_letra_a_letra(self, "Hola", [RED, GREEN, BLUE, YELLOW])
    """
    texto_mobj = Text(texto, font_size=font_size, **kwargs)
    scene.add(texto_mobj)

    letras = texto_mobj.submobjects
    n = min(len(letras), len(colores))
    duracion_por_letra = duracion_total / n if n > 0 else 0

    for i in range(n):
        scene.play(
            letras[i].animate.set_color(colores[i]),
            run_time=duracion_por_letra
        )

############################ Trasformar Grupo[*elementos] ######################

def transformar_objetos_por_etapas(scene, objetos, colores=None, opacidades=None, escalas=None, duracion=2):
    """
    Aplica múltiples transformaciones (color, opacidad, escala) a cada objeto de un grupo,
    uno por uno en secuencia.

    Parámetros:
    - scene: instancia de Scene de Manim.
    - objetos: VGroup o lista de objetos de Manim.
    - colores: lista de colores (opcional).
    - opacidades: lista de valores de opacidad entre 0 y 1 (opcional).
    - escalas: lista de factores de escala (opcional).
    - duracion: tiempo total de la animación.
    """

    n = len(objetos)
    tiempo_por_objeto = duracion / n

    for i, obj in enumerate(objetos):
        animacion = obj.animate
        if colores is not None:
            animacion = animacion.set_color(colores[i])
        if opacidades is not None:
            animacion = animacion.set_opacity(opacidades[i])
        if escalas is not None:
            animacion = animacion.scale(escalas[i])

        scene.play(animacion, run_time=tiempo_por_objeto)
        

def reemplazar_palabra_con_animacion(scene, texto, palabra_a_reemplazar, palabra_nueva,
                                     font_size=48, color_original=WHITE, color_destacado=YELLOW, **kwargs):
    """
    Reemplaza una palabra dentro de un objeto Text usando Transform y resaltando la nueva palabra con color.
    """
    if palabra_a_reemplazar not in texto:
        print(f"La palabra '{palabra_a_reemplazar}' no se encuentra en el texto.")
        return

    # Texto original
    texto_obj = Text(texto, font_size=font_size, color=color_original, **kwargs)
    scene.add(texto_obj)

    # Texto modificado con palabra nueva
    texto_modificado = texto.replace(palabra_a_reemplazar, palabra_nueva)

    # Resaltado con t2c
    t2c = {palabra_nueva: color_destacado}

    texto_nuevo_obj = Text(
        texto_modificado,
        font_size=font_size,
        color=color_original,
        t2c=t2c,
        **kwargs
    )

    # Reemplazo animado
    scene.play(Transform(texto_obj, texto_nuevo_obj), run_time=1.5)
    scene.wait(1)

    ##########################entrada en escena###############################

 def fadein_con_traslacion(objeto: Mobject, desplazamiento: np.ndarray, duracion=1):
    """
    Crea una animación que hace aparecer un objeto con una traslación desde una posición desplazada.

    El objeto aparece (FadeIn) al mismo tiempo que se traslada hacia su posición final.

    Parámetros
    ----------
    objeto : Mobject
        El objeto de Manim que se quiere animar.
    desplazamiento : np.ndarray
        El vector de desplazamiento desde el cual el objeto aparecerá.
    duracion : float, opcional
        Duración de la animación en segundos (por defecto es 1).

    Devuelve
    --------
    tuple
        Una tupla que contiene:
        - Una copia del objeto con su estado inicial preparado.
        - Un AnimationGroup que combina el FadeIn y el desplazamiento.
    """
    objeto_copy = objeto.copy()
    objeto_copy.shift(-desplazamiento)  # Empezar desde atrás

    return objeto_copy, AnimationGroup(
        FadeIn(objeto_copy),
        objeto_copy.animate.shift(desplazamiento),
        lag_ratio=0,
        run_time=duracion
    )


def fadein_con_rotacion(objeto: Mobject, punto_centro: np.ndarray, angulo: float, duracion=1):
    """
    Crea una animación que hace aparecer un objeto con una rotación desde un ángulo inicial.

    El objeto aparece (FadeIn) al mismo tiempo que rota hacia su posición final.

    Parámetros
    ----------
    objeto : Mobject
        El objeto de Manim que se quiere animar.
    punto_centro : np.ndarray
        El punto alrededor del cual se aplicará la rotación.
    angulo : float
        Ángulo en radianes que el objeto rotará desde su posición inicial hasta la final.
        El objeto parte rotado en -ángulo y rota hasta su orientación original.
    duracion : float, opcional
        Duración de la animación en segundos (por defecto es 1).

    Devuelve
    --------
    tuple
        Una tupla que contiene:
        - Una copia del objeto con su estado inicial preparado.
        - Un AnimationGroup que combina el FadeIn y la rotación.
    """
    objeto_copy = objeto.copy()
    objeto_copy.rotate(-angulo, about_point=punto_centro)

    return objeto_copy, AnimationGroup(
        FadeIn(objeto_copy),
        objeto_copy.animate.rotate(angulo, about_point=punto_centro),
        lag_ratio=0,
        run_time=duracion
    )


    ##############################sacar de escena ##############################

    def jalar_objeto(objeto: Mobject, direccion: np.ndarray, duracion=2):
    # Descomponer el objeto en sus submobjects (funciona bien con objetos compuestos como Text o VGroup)
    partes = objeto.submobjects if objeto.submobjects else [objeto]

    animaciones = [
        part.animate.shift(direccion * (0.3 + random.random())).set_opacity(0)
        for part in partes
    ]

    return AnimationGroup(*animaciones, lag_ratio=0.2, run_time=duracion)

    def desintegrar(objeto: Mobject, intensidad=2.0, variacion_angular=PI/6, duracion=2):
    """
    Crea una animación en la que un objeto se desintegra, con sus partes moviéndose
    hacia afuera en direcciones aleatorias y desvaneciéndose.

    Cada subobjeto (o el objeto entero si no tiene submobjects) se traslada desde 
    el centro con una pequeña variación angular aleatoria y se vuelve completamente 
    transparente durante la animación.

    Parámetros
    ----------
    objeto : Mobject
        El objeto de Manim que se desea desintegrar.
    intensidad : float, opcional
        Magnitud del desplazamiento aplicado a cada parte del objeto (por defecto 2.0).
    variacion_angular : float, opcional
        Variación angular aleatoria máxima (en radianes) aplicada a la dirección de salida
        de cada parte (por defecto π/6).
    duracion : float, opcional
        Duración total de la animación (por defecto 2 segundos).

    Devuelve
    --------
    AnimationGroup
        Un grupo de animaciones que mueve y desvanece las partes del objeto simultáneamente.
    """
    partes = objeto.submobjects if objeto.submobjects else [objeto]
    centro = objeto.get_center()
    animaciones = []

    for part in partes:
        direccion = part.get_center() - centro
        if np.linalg.norm(direccion) == 0:
            direccion = np.array([random.uniform(-1,1), random.uniform(-1,1), 0])
        direccion = normalize(direccion)

        angulo_base = math.atan2(direccion[1], direccion[0])
        angulo_desviado = angulo_base + random.uniform(-variacion_angular, variacion_angular)

        dx = math.cos(angulo_desviado)
        dy = math.sin(angulo_desviado)
        direccion_final = np.array([dx, dy, 0])

        desplazamiento = intensidad * direccion_final

        animaciones.append(
            part.animate.shift(desplazamiento).set_opacity(0)
        )

    return AnimationGroup(*animaciones, lag_ratio=0, run_time=duracion)
    
    #####

    def desintegrar_desde_centro(objeto: Mobject, intensidad=2.5, duracion=2):
    """
    Crea una animación en la que las partes del objeto se desintegran radialmente desde el centro,
    distribuyéndose uniformemente en direcciones circulares y desapareciendo.

    Cada subobjeto (o el objeto completo si no tiene submobjects) se desplaza desde el centro
    en una dirección radial distinta y se desvanece gradualmente durante la animación.

    Parámetros
    ----------
    objeto : Mobject
        El objeto de Manim que se desea desintegrar radialmente.
    intensidad : float, opcional
        Magnitud del desplazamiento desde el centro (por defecto 2.5).
    duracion : float, opcional
        Duración total de la animación (por defecto 2 segundos).

    Devuelve
    --------
    AnimationGroup
        Un grupo de animaciones que mueve y desvanece las partes del objeto en direcciones
        uniformemente distribuidas alrededor del centro.
    """
    partes = objeto.submobjects if objeto.submobjects else [objeto]
    centro = objeto.get_center()
    animaciones = []

    n = len(partes)
    if n == 1:
        n = 2

    for i, part in enumerate(partes):
        angulo = i * TAU / n
        direccion = np.array([np.cos(angulo), np.sin(angulo), 0])
        desplazamiento = intensidad * direccion

        animaciones.append(
            part.animate.shift(desplazamiento).set_opacity(0)
        )

    return AnimationGroup(*animaciones, lag_ratio=0, run_time=duracion)


def desintegrar_desde_centro(objeto: Mobject, intensidad=2.5, duracion=2):
    """
    Crea una animación en la que las partes del objeto se desintegran radialmente desde el centro,
    distribuyéndose uniformemente en direcciones circulares y desapareciendo.

    Cada subobjeto (o el objeto completo si no tiene submobjects) se desplaza desde el centro
    en una dirección radial distinta y se desvanece gradualmente durante la animación.

    Parámetros
    ----------
    objeto : Mobject
        El objeto de Manim que se desea desintegrar radialmente.
    intensidad : float, opcional
        Magnitud del desplazamiento desde el centro (por defecto 2.5).
    duracion : float, opcional
        Duración total de la animación (por defecto 2 segundos).

    Devuelve
    --------
    AnimationGroup
        Un grupo de animaciones que mueve y desvanece las partes del objeto en direcciones
        uniformemente distribuidas alrededor del centro.
    """
    partes = objeto.submobjects if objeto.submobjects else [objeto]
    centro = objeto.get_center()
    animaciones = []

    n = len(partes)
    if n == 1:
        n = 2

    for i, part in enumerate(partes):
        angulo = i * TAU / n
        direccion = np.array([np.cos(angulo), np.sin(angulo), 0])
        desplazamiento = intensidad * direccion

        animaciones.append(
            part.animate.shift(desplazamiento).set_opacity(0)
        )

    return AnimationGroup(*animaciones, lag_ratio=0, run_time=duracion)


    ################################ expectativa #############################
    
    def pausar_y_mostrar(texto: str, duracion: float = 2) -> AnimationGroup:
    mensaje = Text(texto).scale(0.8)
    return AnimationGroup(
        FadeIn(mensaje),
        Wait(duracion),
        FadeOut(mensaje),
        lag_ratio=1  # se ejecuta en orden
    )

    ############# capturar estado y restaurarlo #################################

    def capturar_estado(objeto: Mobject) -> Mobject:
    """Devuelve una copia del objeto para guardar su estado visual."""
    return objeto.copy()

def restaurar_estado(escena: Scene, objeto: Mobject, copia: Mobject, dur=1):
    """Restaura el estado del objeto original mediante una animación."""
    escena.play(Transform(objeto, copia), run_time=dur)

    

        