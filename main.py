import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
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
    # Histograma + curva normal teórica
    # Valores de la media (mu) y desviación típica (sigma) de los datos
    mu, sigma = stats.norm.fit(data)

    # Valores teóricos de la normal en el rango observado
    x_hat = np.linspace(min(data), max(data), num=100)
    y_hat = stats.norm.pdf(x_hat, mu, sigma)

    # Gráfico
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x_hat, y_hat, linewidth=2, label='normal')
    ax.hist(x=data, density=True, bins=30, color="#3182bd", alpha=0.5)
    ax.plot(data, np.full_like(data, -0.01), '|k', markeredgewidth=1)
    ax.set_title('Distribución peso mujeres mayores de 15 años')
    ax.set_xlabel('peso')
    ax.set_ylabel('Densidad de probabilidad')
    ax.legend()

    # Gráfico Q-Q
    sm.qqplot(data, line='s')
    plt.title('Gráfico Q-Q')
    plt.show()


if __name__ == '__main__':
    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'Tamaño Panes', 'Tamaño 1')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'Tamaño Panes', 'Tamaño 2')
