from manim import *
"""Clase con funciones auxiliares para las escenas"""

class Herramientas(Scene):
    def crear_logo(self):
        logo = ImageMobject("images\\logorobo.png").scale(0.65)
        logo.move_to(DOWN * 2.80 + LEFT * 5.9).set_opacity(0.55)
        scene.add(logo)
            
    
class Sort(Scene):
    def construct(self):
        c11 = Circle(color=WHITE).shift(UP * 1.5 + LEFT * 2)
        c12 = Circle(color=WHITE).shift(UP * 1.5 + RIGHT * 2)
        c21 = Circle(color=WHITE).shift(DOWN * 1.5 + LEFT * 2)
        c22 = Circle(color=WHITE).shift(DOWN * 1.5 + RIGHT * 2)

        self.play(Write(c11), Write(c12), Write(c21), Write(c22))

        self.play(Swap(c11, c21))

        self.play(Swap(c12, c22, path_arc=160 * DEGREES))
        

class CrearSecuencia(Scene):    
    def construct(self):
        
        def crear_serie_cuadrados(grupo, cuadrado, espaciado, numero):
            for i in range(numero):
                nuevo_cuadrado = cuadrado.copy()
                nuevo_cuadrado.move_to(2 * DOWN + LEFT * 1.5 + i * (cuadrado.side_length + espaciado) * RIGHT)
                grupo.add(nuevo_cuadrado)

            return grupo    
        
        grupo_cuadrados = VGroup()        
        cuadrado = Square(side_length=0.8, fill_color=PINK, fill_opacity=0.75, stroke_width=2)
        cuadrados = crear_serie_cuadrados(grupo_cuadrados, cuadrado, 0.075, 12).shift(2*LEFT)
        self.add(cuadrados)  # Agrega el grupo de cuadrados a la escena
        for i in range(5):
            self.play(cuadrados[i].animate.set_fill(color = RED))

class SVGExample(Scene):
    def construct(self):
        image = SVGMobject("compu.svg")

        self.play(FadeIn(image))

        self.play(image.animate.set_color(WHITE).scale(1.75))

        self.play(Rotate(image, TAU))  # tau = 2 pi

        #self.play(FadeOut(image))
        self.wait(5)

class Rotation3DExample(ThreeDScene):
    def construct(self):
        cube = Cube(side_length=1, fill_opacity=1)
        cube2 = cube.copy().set_color(WHITE).next_to(cube)

        self.begin_ambient_camera_rotation(rate=0.3)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Write(cube), run_time=2)
        self.play(Write(cube2), run_time=2)
        self.wait(3)
        
        #self.play(Unwrite(cube), run_time=2)

class Axes3DExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8)

        # 3D variant of the Dot() object
        dot = Dot3D()

        # zoom out so we see the axes
        self.set_camera_orientation(zoom=0.5)

        self.play(FadeIn(axes), FadeIn(dot), FadeIn(x_label), FadeIn(y_label))

        self.wait(0.5)

        # animate the move of the camera to properly see the axes
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)

        # built-in updater which begins camera rotation
        self.begin_ambient_camera_rotation(rate=0.15)

        # one dot for each direction
        upDot = dot.copy().set_color(RED)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        self.wait(1)

        self.play(
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
        )

        self.wait(2)