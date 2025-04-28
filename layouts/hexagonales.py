#layouts.hexagonales.py
from manim import *
import sys
from pathlib import Path
import numpy as np

# Subir un solo nivel desde la carpeta actual (escenas/horizontales)
root_path = Path().resolve().parents[0]    # parents[0] sería un salto hacia arriba, [1] son dos

# Agregarlo al sys.path si no está ya
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from src.widgets import poligono as pol



class HexagonalField(Scene):
    def construct(self):
        center = np.array([0, 0, 0])
        radius = 0.5  # Radio de cada hexágono
        rows = 7
        cols = 7

        hex_field = self.create_hexagonal_field(center, radius, rows, cols)
        self.add(hex_field)
        self.wait(2)

    def create_hexagonal_field(self, center, radius, rows, cols):
        hexagons = VGroup()

        # Cálculos para distancias
        dx = 3/2 * radius
        dy = np.sqrt(3) * radius

        # Centro inicial
        center_x, center_y, center_z = center

        for row in range(rows):
            for col in range(cols):
                # Posición base
                x = center_x + col * dx
                y = center_y + row * dy

                # Desplazar las filas impares
                if row % 2 == 1:
                    x += (3/4) * radius

                hexagon = RegularPolygon(n=6, radius=radius)
                hexagon.move_to(np.array([x, y, center_z]))

                hexagons.add(hexagon)

        return hexagons

