import os
import pandas as pd
import numpy as np

def muestreo_aceptacion_por_variables_excel(ruta_excel, hoja, K, USL, LSL=None):
    """
    Realiza el muestreo de aceptación por variables utilizando el valor crítico K desde un archivo Excel.

    :param ruta_excel: Ruta al archivo Excel
    :param hoja: Nombre de la hoja dentro del archivo Excel
    :param K: Valor crítico K
    :param USL: Límite Superior de Especificación
    :param LSL: Límite Inferior de Especificación (puede ser None si no se usa)
    :return: DataFrame con los resultados de aceptación para cada columna
    """
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel, sheet_name=hoja)

    # Inicializar una lista para almacenar los resultados
    resultados = []

    # Iterar sobre todas las columnas de la hoja
    for columna in df.columns:
        # Obtener los datos de la columna actual y eliminar NaN
        data = df[columna].dropna().values

        if data.size == 0:
            resultados.append([columna, "No hay datos válidos para análisis", "", ""])
            continue

        # Calcular la media y desviación estándar de la muestra
        x_bar = np.mean(data)
        s = np.std(data, ddof=1)

        # Verificar si el lote cumple con las especificaciones
        accept = True
        if LSL is not None:
            accept &= (x_bar - K * s >= LSL)
        accept &= (x_bar + K * s <= USL)

        # Interpretar el resultado de aceptación
        resultado = "Aceptado" if accept else "No Aceptado"

        # Agregar los resultados a la lista
        resultados.append([columna, resultado, x_bar, s])

    # Crear un DataFrame con los resultados
    resultados_df = pd.DataFrame(resultados,
                                 columns=["Columna", "Resultado de Aceptación", "Media de la muestra", "Desviación estándar"])

    return resultados_df


# Ejemplo de uso
ruta_excel = os.path.join(os.getcwd(), './datos/', 'archivo.xlsx')  # Reemplaza con la ruta correcta a tu archivo Excel
hoja = 'PanesDefecto'
K = 1.45
USL = 6

# Realizar el muestreo de aceptación para todas las columnas
resultados = muestreo_aceptacion_por_variables_excel(ruta_excel, hoja, K, USL)

print("\n")
# Imprimir los resultados
print("Resultados de muestreo de aceptación por variables:")
print(resultados)
