# Análisis Exploratorio del Conjunto de Datos Iris

Este repositorio contiene un análisis exploratorio del famoso conjunto de datos Iris utilizando Python. El análisis incluye la carga de datos, verificación de su estructura, estadísticas descriptivas y visualizaciones de las características del conjunto de datos.

## Archivos

- `datos.py`: Script de Python que realiza el análisis exploratorio y genera las visualizaciones.
- `Iris.csv`: Conjunto de datos Iris.
- `database.sqlite`: Archivo de base de datos (no utilizado en el análisis actual).

## Requisitos

- Python 3.x
- Pandas
- Matplotlib

## Instalación
   ```
1. Instala las dependencias:
   ```bash
   pip install pandas matplotlib
   ```
## Uso

Ejecuta el script `datos.py` para realizar el análisis exploratorio y generar las visualizaciones:
```bash
python datos.py
```

## Salida

El script `datos.py` realiza las siguientes tareas:

1. **Carga de datos** del archivo `Iris.csv`.
2. **Verificación de la estructura de los datos**:
   - Número de filas y columnas.
   - Primeras 5 filas.
   - Información de cada columna.
3. **Análisis exploratorio**:
   - Estadísticas descriptivas.
4. **Visualización de datos**:
   - Histograma de la longitud del sépalo (`SepalLengthCm`).
   - Gráfico de dispersión de la longitud del sépalo (`SepalLengthCm`) frente al ancho del sépalo (`SepalWidthCm`).

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cualquier cambio que te gustaría hacer.
