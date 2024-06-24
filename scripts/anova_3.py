# Importar las librerías necesarias
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Seleccionar el directorio de trabajo
import os
#os.chdir("../Desktop/Clase R/Clase ProgramaciónR/Clase5/")

# Cargar el dataset
tiempo = pd.read_csv("Tiempo.csv")

# Transformar la variable 'metodo' a categórica
tiempo['metodo'] = tiempo['metodo'].astype('category')

# Ver la estructura del dataframe
print(tiempo.info())

# Ver los posibles valores de 'metodo'
print(tiempo['metodo'].unique())
print(tiempo['metodo'].value_counts())

#### Item a ####
# ¿Se verifican los supuestos del modelo de análisis de la varianza?
# Normalidad en la distribución del tiempo en cada uno de los métodos
# Homocedasticidad del tiempo según el método de fabricación
# Independencia de las observaciones

# Diagrama de cajas
sns.boxplot(x='metodo', y='minutos', data=tiempo)
plt.show()

# Pruebas de normalidad: Shapiro-Wilk
for metodo in tiempo['metodo'].unique():
    stat, p = stats.shapiro(tiempo['minutos'][tiempo['metodo'] == metodo])
    print(f'Método {metodo}: p-value = {p}')

# Prueba de homocedasticidad: Bartlett
stat, p = stats.bartlett(*[tiempo['minutos'][tiempo['metodo'] == metodo] for metodo in tiempo['metodo'].unique()])
print(f'Bartlett test: p-value = {p}')

#### Item b ####
# ¿Existe evidencia de que el método influye en el tiempo medio de elaboración del producto?

# ANOVA
model = ols('minutos ~ C(metodo)', data=tiempo).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# Calcular las medias de cada método
print(tiempo.groupby('metodo')['minutos'].mean())

# Representar las diferencias gráficamente
sns.pointplot(x='metodo', y='minutos', data=tiempo, capsize=0.1)
plt.title('Gráfico de medias por grupo')
plt.xlabel('Métodos de Fabricación')
plt.ylabel('Tiempo medio')
plt.show()

#### Item c ####
# Análisis post-hoc: determinar cuáles son los métodos cuyos tiempos medios son diferentes.

# Método de Bonferroni
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(endog=tiempo['minutos'], groups=tiempo['metodo'], alpha=0.05)
print(tukey.summary())

# Graficar resultados de Tukey
tukey.plot_simultaneous()
plt.show()
