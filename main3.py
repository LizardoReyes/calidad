# Anova de 1 factor (CORREGIR)
import os

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Leer el archivo Excel
df = pd.read_excel(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'), sheet_name='PanesDefecto')
# print(df.head())

# Anova de 1 factor
modelo = ols('Croissant ~ C(Croissant)', data=df).fit()
anova_table = sm.stats.anova_lm(modelo, typ=2)
print(anova_table)