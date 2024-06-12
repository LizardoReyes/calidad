import os
import pandas as pd
from scipy import stats


def prueba_kruskal(ruta_excel, hoja):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel, sheet_name=hoja)

    # Imprimir el encabezado de la prueba
    print(f'\nPrueba de Kruskal-Wallis para {hoja}:')

    # Seleccionar todas las columnas de datos no vacías
    columnas_no_vacias = [columna for columna in df.columns if not df[columna].dropna().empty]
    datos = [df[columna].dropna() for columna in columnas_no_vacias]

    if len(datos) < 2:
        print("No hay suficientes columnas con datos para realizar la prueba.")
        return

    # Realizar la prueba de Kruskal-Wallis
    stat, p_value = stats.kruskal(*datos)
    print(f'Estadístico Kruskal-Wallis: {stat}, valor-p: {p_value}')

    # Interpretar el resultado
    if p_value > 0.05:
        print("No hay diferencias significativas entre los grupos (se acepta H0).")
    else:
        print("Hay diferencias significativas entre los grupos (se rechaza H0).")


if __name__ == '__main__':
    prueba_kruskal(os.path.join(os.getcwd(), '../datos/', 'archivo.xlsx'), 'PanesDefecto')
    #prueba_kruskal(os.path.join(os.getcwd(), '../datos/', 'archivo.xlsx'), 'PerdidaPan')
