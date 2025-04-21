
# Renderizar animaciones de Manim en Google Colab

## 1. Crear un nuevo notebook en Google Colab

Abrí [Google Colab](https://colab.research.google.com/) y creá un nuevo notebook.

---

## 2. Instalar Manim

En la primera celda del notebook, ejecutá:

```python
!pip install manim
```

---

## 3. Crear el archivo de tu escena

Usá una celda de código con la magia `%%writefile` para escribir el archivo `.py` con tu escena. Por ejemplo:

```python
%%writefile mi_animacion.py
from manim import *

class MiPrimeraEscena(Scene):
    def construct(self):
        texto = Text("¡Hola desde Manim en Colab!")
        self.play(Write(texto))
        self.wait(1)
```

---

## 4. Renderizar la animación

Luego, ejecutá esta celda para renderizar la escena:

```python
!manim -pql mi_animacion.py MiPrimeraEscena
```

### Parámetros útiles:
- `-p` o `--preview`: Abre el video al terminar (en local; no aplica en Colab).
- `-ql`, `-qm`, `-qh`: Calidad de renderizado (low, medium, high).
- `-r WIDTH,HEIGHT`: Para definir resolución personalizada (por ej. `-r 1920,1080`).

---

## 5. Descargar el archivo de video

El video renderizado se guarda por defecto en `media/videos/mi_animacion/`. Para descargarlo, usá:

```python
from google.colab import files
files.download("media/videos/mi_animacion/480p15/MiPrimeraEscena.mp4")
```

Ajustá la ruta si usás otra calidad o escena.

---

## 6. Consejos adicionales

- Usá `-qh` o `-r 1920,1080` si querés exportar en 1080p para YouTube o reels horizontales.
- Para formato vertical (TikTok, Reels): podés usar `-r 1080,1920`, pero deberás ajustar tus elementos para ese formato en la escena.
- Podés montar tu Google Drive para guardar los renders allí en lugar de descargarlos uno a uno.

```python
from google.colab import drive
drive.mount('/content/drive')
```

Y luego guardar ahí los archivos.

---

¡Listo! Ahora podés usar la potencia de Google Colab para renderizar animaciones sin agotar los recursos de tu máquina.
