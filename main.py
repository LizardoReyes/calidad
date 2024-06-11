import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os


def verificar_normalidad(ruta_excel, hoja, columna):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel, sheet_name=hoja)

    # Seleccionar la columna de datos
    data = df[columna].dropna()  # Asegúrate de manejar los valores NaN si existen
    print(data)

    # Prueba de Shapiro-Wilk
    stat, p_value = stats.shapiro(data)
    print(f'Estadístico Shapiro-Wilk: {stat}, valor-p: {p_value}')

    if data.size > 20:
        # D'Agostino's K-squared test
        stat, p_value = stats.normaltest(data)
        print(f'Estadístico D\'Agostino\'s: {stat}, valor-p: {p_value}')

    # Interpretar el resultado
    if p_value > 0.05:
        print("Los datos parecen seguir una distribución normal (se acepta H0).")
    else:
        print("Los datos no siguen una distribución normal (se rechaza H0).")

    # Visualización
    # Histograma
    plt.hist(data, bins=30, color='lightblue', edgecolor='black')
    plt.title('Histograma')
    plt.show()

    # Gráfico Q-Q
    sm.qqplot(data, line='s')
    plt.title('Gráfico Q-Q')
    plt.show()


if __name__ == '__main__':
    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'Tamaño Panes', 'Tamaño 1')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'Tamaño Panes', 'Tamaño 2')
