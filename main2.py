# Prueba de Kruskal-Wallis
import os

import pandas as pd
from scipy import stats


def prueba_kruskal(ruta_excel, hoja):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel, sheet_name=hoja)
    # print(df.head())

    """
    Prueba de Kruskal-Wallis
    :param data: DataFrame
    :param grupo: str
    :return: None
    """
    print(f'Prueba de Kruskal-Wallis para el grupo')
    print(stats.kruskal(df['Croissant'], df['Cachito relleno'], df['Pizza'],
                        df['Enrollado de canela'], df['Karamanducas'], df['Pan de yema'],
                        df['Empanadas de boda'], df['Enrollados de hot dog'], df['Enrollado de jamón y queso']))
    print('\n')


if __name__ == '__main__':

    prueba_kruskal(os.path.join(os.getcwd(), 'datos/', 'archivo.xlsx'), 'PanesDefecto')