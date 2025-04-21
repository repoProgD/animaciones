# Crear y ejecutar un archivo .py con Manim en Windows usando el prompt de conda

## Paso 1: Activar el entorno virtual

Abrí la terminal de Anaconda y escribí:

# Crear y ejecutar un archivo .py con Manim en Windows usando el prompt de conda

## Paso 1: Activar el entorno virtual

Abrí la terminal de Anaconda y escribí:

```
conda activate nombre_del_entorno
```

Ejemplo:

```
conda activate animaciones
```

---

## Paso 2: Ir al directorio donde guardarás el archivo

Usá `cd` para navegar hasta la carpeta deseada:

```
cd C:\Users\TuUsuario\Ruta\A\La\Carpeta
```

Ejemplo:

```
cd C:\Users\Diego\animaciones
```

---

## Paso 3: Crear el archivo .py con Notepad

Desde la terminal:

```
notepad archivo.py
```

Ejemplo:

```
notepad ejemplo.py
```

Esto abrirá el bloc de notas. Escribí tu código de Manim ahí, guardá y cerrá.

---

## Paso 4: Ejecutar el archivo con Manim

Usá el siguiente comando para renderizar:

```
manim archivo.py NombreDeLaClase -pql
```

Ejemplo:

```
manim ejemplo.py EscenaVertical -pql
```

Donde:
- `archivo.py` es el archivo que creaste.
- `NombreDeLaClase` es el nombre de la escena dentro del archivo.
- `-pql` indica "preview" + "quality low" (render rápido).

---

## Extras útiles

- `-pql`: preview + calidad baja
- `-pqh`: preview + calidad alta
- `--disable_caching`: fuerza el render completo sin usar caché

