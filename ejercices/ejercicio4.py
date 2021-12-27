import datetime

import pandas as pd

"""
En esta opción tendremos que calcular la ganancia entre dos períodos de tiempo
"""
import config.configuration


def exercice_4(company_name, period1, period2):
    values = pd.read_csv(config.configuration.get_url(company_name, period1, period2))
    first_value = values.iloc[0]['Close']
    last_value = values.iloc[-1]['Close']
    profit = last_value - first_value
    return profit


def exercice_4_pretty():
    check = True
    while check:
        company_name = input('Introduzca el nombre de la empresa: ')
        check = not config.configuration.check_company_in_market(company_name)
        if check:
            print('El nombre de esa compañía no está disponible en el mercado, inténtelo de nuevo.')
    check = True
    while check:
        period1 = input('Introduzca la fecha de inicial (formato dd/mm/yyyy): ')
        check = validate_date(period1)
    check = True
    while check:
        period2 = input('Introduzca la fecha de final (formato dd/mm/yyyy): ')
        check = validate_date(period2)
    profit = exercice_4(company_name, period1, period2)
    print('Por cada acción vendida, el beneficio ha sido de {}€'.format(profit))


def validate_date(date_text):
    res = False
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        res = True
        print('El formato de fecha introducido es incorrecto')
    return res
