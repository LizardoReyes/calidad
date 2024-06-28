import os
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.stats.multicomp as mc
import matplotlib.pyplot as plt

def anova_1_factor_2(ruta_excel, hoja):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel, sheet_name=hoja)

    # Preparar los datos para el ANOVA
    df_melt = df.melt(var_name='Tratamiento', value_name='Valor').dropna()

    # Ajustar el modelo lineal
    modelo = ols('Valor ~ C(Tratamiento)', data=df_melt).fit()
    anova_resultado = sm.stats.anova_lm(modelo, typ=2)
    print(f'\nANOVA de 1 factor para {hoja}:')
    print(anova_resultado)

    # Prueba de normalidad de los residuos
    residuos = modelo.resid
    stat, p_value = stats.shapiro(residuos)
    print(f'\nPrueba de Shapiro-Wilk para los residuos:')
    print(f'Estadístico: {stat}, valor-p: {p_value}')
    if p_value > 0.05:
        print("Los residuos parecen seguir una distribución normal (se acepta H0).")
    else:
        print("Los residuos no siguen una distribución normal (se rechaza H0).")

    # Prueba de igualdad de varianzas (Prueba de Levene)
    stat, p_value = stats.levene(*[df[col].dropna() for col in df.columns])
    print(f'\nPrueba de Levene para igualdad de varianzas:')
    print(f'Estadístico: {stat}, valor-p: {p_value}')
    if p_value > 0.05:
        print("Se cumple la igualdad de varianzas entre los grupos (se acepta H0).")
    else:
        print("No se cumple la igualdad de varianzas entre los grupos (se rechaza H0).")

    # Comparaciones múltiples post-hoc (Tukey HSD)
    comparaciones = mc.MultiComparison(df_melt['Valor'], df_melt['Tratamiento'])
    tukey_resultado = comparaciones.tukeyhsd()
    print(f'\nComparaciones múltiples post-hoc (Tukey HSD):')
    print(tukey_resultado)

    # Gráfico de las comparaciones múltiples post-hoc (Tukey HSD)
    fig, ax = plt.subplots(figsize=(10, 6))
    tukey_resultado.plot_simultaneous(ax=ax)
    ax.axvline(x=0, color='grey', linestyle='--')
    plt.title(f'Comparaciones múltiples post-hoc (Tukey HSD) para {hoja}')
    plt.show()

if __name__ == '__main__':
    # Ruta al archivo Excel
    ruta_excel = os.path.join(os.getcwd(), '../datos/', 'archivo.xlsx')

    # Realizar el ANOVA para cada hoja
    anova_1_factor_2(ruta_excel, 'PanesDefecto')
    # anova_1_factor_2(ruta_excel, 'PerdidaPan')
