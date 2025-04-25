from manim import config


# Guardamos valores originales por si queremos revertir
ALTURA_ORIGINAL = config.pixel_height
ANCHO_ORIGINAL = config.pixel_width

# Intercambiamos resolución para formato vertical
config.pixel_height = 1920
config.pixel_width = 1080

# Ajustamos frame en proporción 9:16 (ancho:alto)
config.frame_width =  9
config.frame_height = 16

# Variables útiles para importar
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

# Imprimir para verificar
print(f"Frame dimensions: {FRAME_WIDTH}x{FRAME_HEIGHT}")
print(f"Resolution: {config.pixel_width}x{config.pixel_height}")

