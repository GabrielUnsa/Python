# Documentación: dirPathStructure.py

## Propósito

`dirPathStructure.py` recorre recursivamente una carpeta dada y genera un archivo Excel (`Tree.xlsx`) que contiene la estructura de directorios y archivos organizados por niveles (Nivel 1, Nivel 2, ...).

## Dependencias

- Python 3.7+
- pandas
- openpyxl (usado por pandas para escribir archivos Excel)

Puedes instalar dependencias con pip:

```powershell
pip install pandas openpyxl
```

## Uso

Ejecuta el script y proporciona la ruta de la carpeta cuando se te solicite:

```powershell
python dirPathStructure.py
# Luego ingresa la ruta cuando se te pregunte:
# Ingrese la ruta de la carpeta: C:\Mi\Carpeta\AExplorar
```

El script creará `Tree.xlsx` en el directorio de trabajo actual.

## Descripción del código

Archivo: `dirPathStructure.py`

Función principal: `traversal_path(directory, current_path=None, rows=None)`

- Parámetros:
  - `directory` (str): ruta absoluta o relativa del directorio a recorrer.
  - `current_path` (list, opcional): lista que contiene los nombres de los niveles actuales (se utiliza durante la recursión).
  - `rows` (list, opcional): lista acumulativa que almacena cada fila (cada fila representa una ruta hasta un archivo o directorio).

- Comportamiento:
  - Si `current_path` o `rows` es `None`, la función inicializa valores vacíos.
  - Lista los ítems del directorio actual ordenados alfabéticamente.
  - Añade una fila con la `current_path` actual (esto registra la carpeta en sí)
  - Para cada ítem:
    - Si es un subdirectorio, llama recursivamente a `traversal_path` con `current_path + [item]`.
    - Si es archivo, añade una fila `current_path + [item]`.
  - Devuelve `rows`, que es una lista de listas.

Flujo cuando se ejecuta directamente (`if __name__ == "__main__":`)

1. Pide al usuario la ruta de la carpeta.
2. Valida que exista y que sea un directorio.
3. Llama a `traversal_path(folder, [os.path.basename(folder)])` para obtener todas las rutas.
4. Calcula `max_levels` (la longitud máxima de las filas) y normaliza todas las filas rellenando con cadenas vacías para que tengan la misma longitud.
5. Genera nombres de columnas `Nivel 1`, `Nivel 2`, ... según `max_levels`.
6. Construye un DataFrame de pandas y lo exporta a `Tree.xlsx`.

## Ejemplo de salida

Si la estructura es:

```
Proyecto/
├─ src/
│  ├─ main.py
│  └─ utils.py
└─ README.md
```

`Tree.xlsx` tendrá filas parecidas a:

- Nivel 1 | Nivel 2 | Nivel 3
- Proyecto | src | 
- Proyecto | src | main.py
- Proyecto | src | utils.py
- Proyecto | README.md |

## Notas
- Asegúrate de tener permisos de lectura en la carpeta que deseas explorar.
- El archivo Excel se sobrescribirá si ya existe en el directorio de trabajo actual.
- El programa fue diseñado para realizar tree del directorio con el objetivo de documentar la estructura de carpetas y archivos y luego procesar la salida en otro programa.

## Autor
@Gabi

## Colaboradores Y Agradecimientos
@GitHub Copilot sugerencias y ayuda en la generación del código.