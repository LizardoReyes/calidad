# Anova de 1 factor (CORREGIR)
import os

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols


def anova_1_factor(df):
    # Calculamos medias
    #print(f'\nMedias')
    #print(df.mean())
    # Calculamos desviaciones
    #print(f'\nDesviaciones')
    #print(df.std())

    # Anova de 1 factor
    print(f'Anova de 1 factor')
    anova_result = stats.f_oneway(df['Croissant'], df['Cachito relleno'], df['Pizza'], df['Enrollado de canela'],
                                  df['Karamanducas'], df['Pan de yema'], df['Empanadas de boda'],
                                  df['Enrollados de hot dog'], df['Enrollado de jamón y queso'])

    print(anova_result)


if __name__ == '__main__':
    # Leer el archivo Excel
    #df = pd.read_excel(os.path.join(os.getcwd(), '../datos/', 'archivo.xlsx'), sheet_name='PanesDefecto')
    #anova_1_factor(df)

    df = pd.read_excel(os.path.join(os.getcwd(), '../datos/', 'archivo.xlsx'), sheet_name='PerdidaPan')
    anova_1_factor(df)
