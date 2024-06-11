import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import os


def verificar_normalidad(ruta_excel, hoja, columna):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel, sheet_name=hoja)
    # print(df.head())

    # Seleccionar la columna de datos
    data = df[columna].dropna()  # Asegúrate de manejar los valores NaN si existen
    # print(data)

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
                         'PanesDefecto', 'Croissant')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Cachito relleno')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Pizza')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Enrollado de canela')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Karamanducas')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Pan de yema')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Empanadas de boda')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Enrollados de hot dog')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PanesDefecto', 'Enrollado de jamón y queso')



    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Croissant')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Cachito relleno')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Pizza')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Enrollado de canela')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Karamanducas')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Pan de yema')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Empanadas de boda')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Enrollados de hot dog')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Enrollado de jamón y queso')

    verificar_normalidad(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'),
                         'PerdidaPan', 'Enrollado de jamón y queso')
