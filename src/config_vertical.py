from manim import config


# altura_default = config.pixel_height
# ancho_default = config.pixel_width
# config.pixel_height = config.pixel_width
# config.pixel_width = altura_default

# Guardamos valores originales por si queremos revertir
ALTURA_ORIGINAL = config.pixel_height
ANCHO_ORIGINAL = config.pixel_width

# Intercambiamos resolución para formato vertical
config.pixel_height = ANCHO_ORIGINAL
config.pixel_width = ALTURA_ORIGINAL

# Ajustamos frame en proporción 9:16 (ancho:alto)
config.frame_width = config.frame_height * (9 / 16)

# Variables útiles para importar
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


# # Cambio del frame para ajustarse al cambio de resolución
# config.frame_width = config.frame_height * (9/16)
# FRAME_HEIGHT = config.frame_height
# FRAME_WIDTH = config.frame_width