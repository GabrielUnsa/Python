# Python — Aprendizaje con libros y cursos

Colección de notebooks y ejercicios que realicé como parte de mi aprendizaje personal de Python mediante **libros y cursos**. El material documenta prácticas de TensorFlow, aprendizaje automático, redes neuronales y uso de APIs de inteligencia artificial.

Los ejemplos reflejan distintas etapas de ese aprendizaje y conservan apuntes, experimentos y resultados de ejecuciones anteriores. Cada notebook tiene sus propios datos, dependencias y entorno de trabajo.

## Contenido

- [Estructura](#estructura)
- [Fundamentos de TensorFlow y prácticas de cursos](#fundamentos-de-tensorflow-y-prácticas-de-cursos)
- [Aprendizaje automático con TensorFlow](#aprendizaje-automático-con-tensorflow)
- [Gemini y agentes de inteligencia artificial](#gemini-y-agentes-de-inteligencia-artificial)
- [Datos de práctica](#datos-de-práctica)
- [Preparación y uso](#preparación-y-uso)
- [Estado y compatibilidad](#estado-y-compatibilidad)
- [Licencia](#licencia)

## Estructura

```text
.
├── jupyter-notebooks/
│   ├── tensorFlow/
│   │   └── TensorFlow Basic.ipynb
│   └── edx/tensorFlow/
│       ├── M1 - Introduccion tf/
│       │   ├── Hellow World.ipynb
│       │   ├── LinealRegression.ipynb
│       │   └── LogisticRegression.ipynb
│       └── M2 - Introduccion a CNNs/
│           ├── CNN.ipynb
│           └── ReviewCNN.ipynb
├── Machine Learning/
│   ├── TensorFlow 2.ipynb
│   └── Datasets/
│       ├── sales_data.csv
│       ├── stories.txt
│       └── weather dataset/
│           ├── train/
│           ├── validation/
│           └── test/
├── API's IA Learning/
│   └── Introduccion Gemini & Agent AI/
│       ├── Introduccion a API GEMINI - IA.ipynb
│       └── Agent AI con CrewIA.ipynb
├── LICENSE
└── README.md
```

## Fundamentos de TensorFlow y prácticas de cursos

La carpeta [jupyter-notebooks](jupyter-notebooks/) reúne ejemplos introductorios y prácticas organizadas en módulos dentro de `edx/tensorFlow/`.

| Notebook | Contenido |
| --- | --- |
| [TensorFlow Basic.ipynb](jupyter-notebooks/tensorFlow/TensorFlow%20Basic.ipynb) | Operaciones básicas con tensores, conversión desde NumPy, comparación de multiplicaciones matriciales en CPU y GPU cuando está disponible, y creación de conjuntos de datos con `tf.data`. |
| [Hellow World.ipynb](jupyter-notebooks/edx/tensorFlow/M1%20-%20Introduccion%20tf/Hellow%20World.ipynb) | Constantes, variables, escalares, vectores, matrices, operaciones aritméticas y funciones con `tf.function`. |
| [LinealRegression.ipynb](jupyter-notebooks/edx/tensorFlow/M1%20-%20Introduccion%20tf/LinealRegression.ipynb) | Regresión lineal sobre datos de consumo de combustible y emisiones. Descarga un CSV y ajusta parámetros mediante gradientes con `tf.GradientTape`. |
| [LogisticRegression.ipynb](jupyter-notebooks/edx/tensorFlow/M1%20-%20Introduccion%20tf/LogisticRegression.ipynb) | Clasificación multiclase sobre Iris, preparación de etiquetas, separación de entrenamiento y prueba, optimización y evaluación. |
| [CNN.ipynb](jupyter-notebooks/edx/tensorFlow/M2%20-%20Introduccion%20a%20CNNs/CNN.ipynb) | Clasificación de dígitos de MNIST con aplanamiento de imágenes, una transformación lineal y salida softmax. Aunque está en el módulo de CNN, el modelo de este archivo no utiliza capas convolucionales. |
| [ReviewCNN.ipynb](jupyter-notebooks/edx/tensorFlow/M2%20-%20Introduccion%20a%20CNNs/ReviewCNN.ipynb) | Convolución en una y dos dimensiones, padding, filtros y mapas de características con NumPy, SciPy y TensorFlow. Incluye procesamiento de imágenes descargadas. |

Los módulos conservan celdas de instalación con `tensorflow==2.2.0` y `grpcio==1.24.3`. Esas versiones forman parte del entorno original de los ejercicios; deben revisarse antes de ejecutar las instalaciones en otro entorno.

## Aprendizaje automático con TensorFlow

[TensorFlow 2.ipynb](Machine%20Learning/TensorFlow%202.ipynb) es el notebook más extenso del repositorio. Contiene apuntes y experimentos organizados por capítulos, con una referencia dentro del propio archivo al repositorio del libro **TensorFlow Developer Certificate Guide**.

| Área | Ejercicios incluidos |
| --- | --- |
| Fundamentos | Creación, transformación y agregación de tensores; operaciones matriciales y primeros modelos con Keras. |
| Regresión | Predicción de salarios, escalado de datos, comparación de modelos, evaluación y guardado de modelos. |
| Clasificación | Clasificación de abandono estudiantil y de imágenes de Fashion-MNIST, con preparación de datos y métricas. |
| Redes convolucionales | Clasificación de imágenes meteorológicas, comparación de arquitecturas y seguimiento del entrenamiento. |
| Mejora de modelos | Early stopping, regularización, dropout, aumento de datos y ajustes de la tasa de aprendizaje. |
| Transferencia de aprendizaje | Experimentos con imágenes de radiografías y redes preentrenadas, incluidas InceptionV3 y MobileNet. |
| Procesamiento de texto | Limpieza, tokenización, secuencias, padding, embeddings, análisis de sentimiento con Yelp y clasificación de noticias con AG News. |
| Modelos de secuencias | Comparación de redes recurrentes, LSTM y GRU, uso de embeddings GloVe y generación de historias. |
| Series temporales | Pronóstico de ventas, métodos ingenuos, medias móviles, diferencias, ventanas temporales, redes neuronales y descarga de cotizaciones mediante `yfinance`. |

Las secciones reutilizan nombres de variables y modelos. Para estudiar un capítulo conviene revisar sus celdas de preparación y ejecutar la sección en orden, con un kernel limpio cuando se cambia de experimento.

## Gemini y agentes de inteligencia artificial

La carpeta [Introduccion Gemini & Agent AI](API%27s%20IA%20Learning/Introduccion%20Gemini%20%26%20Agent%20AI/) contiene dos prácticas de uso de modelos mediante APIs.

| Notebook | Contenido |
| --- | --- |
| [Introduccion a API GEMINI - IA.ipynb](API%27s%20IA%20Learning/Introduccion%20Gemini%20%26%20Agent%20AI/Introduccion%20a%20API%20GEMINI%20-%20IA.ipynb) | Primeras solicitudes con `google.genai`, configuración de parámetros, entrada con imágenes, generación de código, plantillas de prompts y ejemplos de tutoría de inglés. Incluye una demostración de recuperación de contexto desde un diccionario local. |
| [Agent AI con CrewIA.ipynb](API%27s%20IA%20Learning/Introduccion%20Gemini%20%26%20Agent%20AI/Agent%20AI%20con%20CrewIA.ipynb) | Uso de CrewAI con dos agentes: un profesor de inglés que explica un tema y un evaluador que genera preguntas. Define sus tareas, configura Gemini como modelo y ejecuta el conjunto mediante `crew.kickoff()`. |

La demostración de recuperación de contexto busca coincidencias de palabras en un diccionario y agrega el texto encontrado al prompt. No incluye una base vectorial ni un sistema de embeddings.

Los notebooks solicitan la clave de Gemini mediante `getpass`. Requieren acceso al servicio y una configuración de modelos válida para la cuenta utilizada. Los identificadores de modelos presentes en las celdas corresponden a los experimentos guardados; su disponibilidad no se verificó al preparar esta documentación.

## Datos de práctica

La carpeta [Machine Learning/Datasets](Machine%20Learning/Datasets/) incluye:

| Recurso | Descripción |
| --- | --- |
| [sales_data.csv](Machine%20Learning/Datasets/sales_data.csv) | 3.653 registros con las columnas `Date` y `Sales`, utilizados en ejercicios de series temporales. |
| [stories.txt](Machine%20Learning/Datasets/stories.txt) | Texto para los experimentos de generación de historias. |
| [weather dataset](Machine%20Learning/Datasets/weather%20dataset/) | 1.125 archivos de imágenes distribuidos en entrenamiento, validación y prueba, con las clases `cloud`, `rain`, `shine` y `sunrise`. |

Distribución de los archivos de imágenes incluidos:

| Partición | cloud | rain | shine | sunrise | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| `train` | 207 | 152 | 189 | 243 | 791 |
| `validation` | 59 | 33 | 35 | 52 | 179 |
| `test` | 35 | 30 | 29 | 61 | 155 |

Otros datos se obtienen desde las celdas mediante URLs, conjuntos de TensorFlow/Keras, TensorFlow Datasets, KaggleHub o `yfinance`. Esas descargas y los modelos generados durante el entrenamiento no forman parte del conjunto de datos local descrito arriba.

## Preparación y uso

Los archivos `.ipynb` se utilizan desde JupyterLab u otro entorno compatible con notebooks. Varias secciones también contienen código específico de Google Colab o Kaggle.

### Entorno local

Los siguientes comandos usan Bash y parten de la carpeta donde se quiera clonar el repositorio. Se necesita Python 3 con soporte de entornos virtuales y una versión compatible con las bibliotecas del notebook elegido.

```bash
git clone https://github.com/GabrielUnsa/Python.git
cd Python
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyterlab ipykernel
python -m ipykernel install --user --name python-aprendizaje \
  --display-name "Python - Aprendizaje"
```

Instalar las dependencias del grupo que se quiera explorar. Para los ejemplos de TensorFlow y análisis de datos:

```bash
python -m pip install tensorflow numpy pandas matplotlib seaborn scipy scikit-learn pillow
```

Algunas secciones del notebook extenso agregan otras bibliotecas:

```bash
python -m pip install tensorflow-datasets tensorflow-hub kagglehub beautifulsoup4 requests yfinance
```

Para las prácticas de Gemini y CrewAI:

```bash
python -m pip install google-genai crewai litellm requests pillow
```

Estas listas reflejan las importaciones del material y no constituyen un entorno con versiones fijadas. El notebook de CrewAI instala `google-generativeai`, pero importa `from google import genai`; se debe revisar esa celda y disponer de `google-genai` para esa importación.

Abrir el entorno desde la raíz del repositorio:

```bash
python -m jupyterlab
```

Seleccionar el kernel **Python - Aprendizaje**, abrir un notebook y revisar sus celdas de instalación y carga de datos antes de ejecutarlo.

### Ajuste de rutas

`TensorFlow 2.ipynb` conserva rutas de Google Drive bajo `/content/drive/MyDrive/...` y de Kaggle bajo `/kaggle/input/...`. Para usar los datos incluidos localmente, sustituir esas rutas y omitir las celdas de montaje de Drive.

Por ejemplo, si el directorio de trabajo del kernel es `Machine Learning/`, las rutas de imágenes pueden definirse como:

```python
from pathlib import Path

datos = Path("Datasets")
train_dir = str(datos / "weather dataset" / "train")
val_dir = str(datos / "weather dataset" / "validation")
test_dir = str(datos / "weather dataset" / "test")
```

En ese mismo directorio, los otros archivos locales se encuentran en `Datasets/sales_data.csv` y `Datasets/stories.txt`. Si el kernel trabaja desde otra carpeta, hay que ajustar el prefijo de las rutas.

## Estado y compatibilidad

Se revisó el contenido de los nueve notebooks, se comprobó que sus archivos JSON tienen la estructura básica de un notebook de versión 4 y se verificaron los nombres, columnas y cantidades de los datos locales. Esta comprobación no equivale a ejecutar las celdas ni a validar los resultados guardados.

El entorno de documentación no tenía TensorFlow ni Jupyter instalados. No se instalaron dependencias, no se entrenaron modelos, no se realizaron descargas externas ni se enviaron solicitudes a las APIs.

El material conserva detalles que requieren revisión al reproducir los ejercicios:

- Las versiones antiguas de las celdas de instalación y las dependencias sin versiones fijadas no definen un único entorno reproducible.
- Algunas celdas requieren comandos externos como `wget` o `unzip`. En la sección de radiografías aparece `!wegt` y una llamada a `unrar` sobre un archivo `.zip`, que deben corregirse antes de usar esa descarga.
- La primera configuración del conjunto meteorológico en `TensorFlow 2.ipynb` intercambia las rutas de entrenamiento y prueba; otra sección posterior las define con sus nombres correspondientes. Se deben comprobar las particiones antes de entrenar y evaluar.
- Las celdas con rutas de Colab o Kaggle y las descargas de datos requieren adaptarse al entorno elegido.
- Los modelos guardados como `.h5` y las salidas de embeddings se generan al ejecutar las celdas. Los resultados visibles en los notebooks corresponden a ejecuciones anteriores.

No hay una aplicación principal, un archivo común de dependencias ni una suite de pruebas automatizadas. El repositorio se organiza como material de estudio para ejecutar y modificar por secciones.

## Licencia

El repositorio incluye una [licencia MIT](LICENSE). Copyright © 2025 Gabriel Marmanillo.
