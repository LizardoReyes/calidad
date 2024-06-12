import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import os

def verificar_normalidad_2(ruta_excel, hoja):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel, sheet_name=hoja)

    # Inicializar una lista para almacenar los resultados
    resultados = []

    # Iterar sobre todas las columnas de la hoja
    for columna in df.columns:
        # Seleccionar la columna de datos
        data = df[columna].dropna()  # Asegúrate de manejar los valores NaN si existen

        if data.empty:
            resultados.append([columna, "La columna está vacía o solo contiene valores NaN.", "", ""])
            continue

        # Prueba de Kolmogorov-Smirnov
        stat_ks, p_value_ks = stats.kstest(data, 'norm', args=(data.mean(), data.std()))

        # Interpretar el resultado
        resultado_ks = "Normal" if p_value_ks > 0.05 else "No Normal"

        # Agregar los resultados a la lista
        resultados.append([columna, stat_ks, p_value_ks, resultado_ks])

    # Crear un DataFrame con los resultados
    resultados_df = pd.DataFrame(resultados, columns=["Columna", "Kolmogorov-Smirnov Estadístico", "Kolmogorov-Smirnov p-valor", "Resultado Kolmogorov-Smirnov"])

    # Imprimir la tabla de resultados
    print(resultados_df)

def graficar(data):
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
    ax.set_title('Distribución de los datos')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad de probabilidad')
    ax.legend()

    # Gráfico Q-Q
    sm.qqplot(data, line='s')
    plt.title('Gráfico Q-Q')
    plt.show()

if __name__ == '__main__':
    # Verificar normalidad y graficar para las hojas especificadas
    print('\nVerificación de normalidad para PanesDefecto')
    verificar_normalidad_2(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), 'PanesDefecto')

    # Para verificar la hoja 'PerdidaPan', descomentar la siguiente línea:
    #print('\nVerificación de normalidad para PerdidaPan')
    #verificar_normalidad_2(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), 'PerdidaPan')
