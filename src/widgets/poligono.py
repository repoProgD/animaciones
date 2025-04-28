from manim import *

class PolygonWidget(VGroup):
    def __init__(self, center, radius, num_sides, **kwargs):
        super().__init__(**kwargs)

        # Guardar parámetros
        self.center = center
        self.radius = radius
        self.num_sides = num_sides

        # Crear los vértices del polígono
        self.vertices = self._get_polygon_vertices()

        # Crear el polígono a partir de los vértices
        self.polygon = Polygon(*self.vertices, color=BLUE, fill_color=BLUE, fill_opacity=0.5)

        # Añadir el polígono al widget
        self.add(self.polygon)

    def _get_polygon_vertices(self):
        """Genera los vértices de un polígono regular"""
        angle_step = TAU / self.num_sides
        vertices = []
        for i in range(self.num_sides):
            angle = angle_step * i
            x = self.center[0] + self.radius * np.cos(angle)
            y = self.center[1] + self.radius * np.sin(angle)
            vertices.append(np.array([x, y, 0]))
        return vertices

    def update_polygon(self, center=None, radius=None, num_sides=None):
        """Actualiza el polígono con nuevos parámetros"""
        if center is not None:
            self.center = center
        if radius is not None:
            self.radius = radius
        if num_sides is not None:
            self.num_sides = num_sides

        # Actualizar los vértices
        self.vertices = self._get_polygon_vertices()

        # Actualizar la forma del polígono
        self.polygon.set_points_as_corners(self.vertices)

        self[0] = self.polygon  # Reemplazar el polígono anterior

