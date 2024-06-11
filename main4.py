# Correlacion Spearman

import numpy as np
import pandas as pd
from scipy import stats
import os

# Leer el archivo Excel
df = pd.read_excel(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'), sheet_name='PanesDefecto')
# print(df.head())

# Correlacion Spearman
print(f'Correlacion Spearman')
print(stats.spearmanr(df['Croissant'], df['Cachito relleno']))
print(stats.spearmanr(df['Croissant'], df['Pizza']))
print(stats.spearmanr(df['Croissant'], df['Enrollado de canela']))
print(stats.spearmanr(df['Croissant'], df['Karamanducas']))
print(stats.spearmanr(df['Croissant'], df['Pan de yema']))
print(stats.spearmanr(df['Croissant'], df['Empanadas de boda']))
print(stats.spearmanr(df['Croissant'], df['Enrollados de hot dog']))
print(stats.spearmanr(df['Croissant'], df['Enrollado de jamón y queso']))
