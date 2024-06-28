import os

import pandas as pd

from scripts.anova_1_factor import anova_1_factor
from scripts.anova_1_factor_2 import anova_1_factor_2
from scripts.kruskal_wallis import prueba_kruskal
from scripts.normalidad import verificar_normalidad
from scripts.normalidad2 import verificar_normalidad_2

if __name__ == '__main__':

    """
    # Prueba de normalidad Kolmogorov-Smirnov
    print("\nPrueba de normalidad Kolmogorov-Smirnov\n")
    verificar_normalidad_2(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), 'PanesDefecto')

    # Prueba de normalidad Shapiro-Wilk
    print("\nPrueba de normalidad Shapiro-Wilk\n")
    verificar_normalidad(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), 'PanesDefecto')
    """


    '''
    # Prueba de kruskal wallis
    print("\nPrueba de Kruskal-Wallis")
    prueba_kruskal(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), 'PanesDefecto')
    '''


    '''
    ### SEGUNDO ###

    # Prueba de normalidad Shapiro-Wilk
    print("\nPrueba de normalidad Shapiro-Wilk\n")
    verificar_normalidad(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), 'PerdidaPan')

    # Prueba de normalidad Kolmogorov-Smirnov
    print("\nPrueba de normalidad Kolmogorov-Smirnov\n")
    verificar_normalidad_2(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), 'PerdidaPan')
    '''



    # Prueba de Anova 1 factor
    ruta_excel = os.path.join(os.getcwd(), './datos/', 'archivo.xlsx')
    anova_1_factor_2(ruta_excel, 'PerdidaPan')

    # Prueba de Anova 1 factor
    df = pd.read_excel(os.path.join(os.getcwd(), './datos/', 'archivo.xlsx'), sheet_name='PerdidaPan')
    anova_1_factor(df)

