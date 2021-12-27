from os import path

import pandas as pd
import config.configuration
from dateutil.parser import parse
import datetime as dt

"""
RESUMEN: Mostrar las empresas de las que hemos tenido acciones y mostrar el valor actual
El objetivo de esta actividad es hacer un programa en el que:

    1. En primer lugar localizaremos nuestro archivo y filtraemos todas las compañías que hemos tenido
    2. Por cada una de ellas realizaremos una búsqueda de su valor actual y crearemos una tupla con el nombre de la compañia y su valor actual
    3. Ordenamos la lista de más a menos valor
"""


def exercice_3():
    directory = config.configuration.transaction_directory
    res = []
    if path.exists(directory):
        companies = pd.read_csv(directory)['company_name'].unique()
        for company in companies:
            res.append([company, get_current_value(company)])
        print(res)
    else:
        print('No ha comprado nunca ninguna acción. No hay ningún regristro que mostrar.')


def get_current_value(company_name):
    url = config.configuration.get_url_current_value(company_name)
    value = pd.read_csv(url)['Adj Close'][0]
    return value
