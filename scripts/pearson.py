# Correlacion Pearson

import numpy as np
import pandas as pd
from scipy import stats
import os


def pearson(df):
    # Correlacion Pearson
    print(f'Correlacion Pearson')
    print(stats.pearsonr(df['Croissant'], df['Cachito relleno']))
    print(stats.pearsonr(df['Croissant'], df['Pizza']))
    print(stats.pearsonr(df['Croissant'], df['Enrollado de canela']))
    print(stats.pearsonr(df['Croissant'], df['Karamanducas']))
    print(stats.pearsonr(df['Croissant'], df['Pan de yema']))
    print(stats.pearsonr(df['Croissant'], df['Empanadas de boda']))
    print(stats.pearsonr(df['Croissant'], df['Enrollados de hot dog']))
    print(stats.pearsonr(df['Croissant'], df['Enrollado de jamón y queso']))
    print('\n')


if __name__ == '__main__':
    # Leer el archivo Excel
    df = pd.read_excel(os.path.join(os.getcwd(), '../datos/', 'archivo.xlsx'), sheet_name='PanesDefecto')
    # print(df.head())
    pearson(df)
