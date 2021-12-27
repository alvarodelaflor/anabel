import time, datetime
import pandas as pd

from exercices import ejercicio4, ejercicio1, ejercicio3, ejercicio2

base_url = 'https://query1.finance.yahoo.com/v7/finance/download/'
destination_folder = './data/'
transaction_directory = 'data/transactions.csv'


def get_url(company_name, period1, period2):
    return base_url + str(company_name) + '?period1=' + str(calculate_date(period1)) + '&period2=' + str(calculate_date(period2)) + '&interval=1d' \
                                                                                                    '&events=history' \
                                                                                                    '&includeAdjustedClose=true'


def get_url(company_name, period1, period2):
    return base_url + str(company_name) + '?period1=' + str(calculate_date(period1)) + '&period2=' + str(calculate_date(period2)) + '&interval=1d' \
                                                                                                    '&events=history' \
                                                                                                    '&includeAdjustedClose=true'


def get_url_current_value(company_name):
    return base_url + str(company_name)


def get_transaction_directory():
    return transaction_directory


def get_dest_folder():
    return destination_folder


def calculate_date(date):
    return str(time.mktime(datetime.datetime.strptime(str(date), "%d/%m/%Y").timetuple()))[:-2]


def check_company_in_market(company_name):
    res = True
    try:
        pd.read_csv(get_url_current_value(company_name))
    except:
        res = False
    return res


def select_option():
    valid_values = [str(x) for x in range(5)]
    value = -1
    repeat = True
    while repeat:
        while value == -1:
            value = input('Seleccione la opción que desee: \n'
                          '    1 - Comprar acciones\n'
                          '    2 - Vender acciones\n'
                          '    3 - Historial de mis acciones\n'
                          '    4 - Ganancia entre dos períodos de tiempo\n'
                          'Decisión: ')
            if value not in valid_values:
                print('Valor inválido, inténtelo otra vez')
                value = -1
            else:
                print('Genial, ha elegido: ' + value)
                application_orchestrator(int(value))
                value = 0
        ask = input('¿Desea realizar otra operación? Escriba "s" si lo desea, cualquier otra tecla en caso contrario\nDecisión:')
        if ask != "s":
            repeat = False
        else:
            value = -1


def application_orchestrator(value):
    if value == 1:
        ejercicio1.exercice_1()
    elif value == 2:
        ejercicio2.exercice_2()
    elif value == 3:
        ejercicio3.exercice_3()
    elif value == 4:
        ejercicio4.exercice_4_pretty()
    else:
        print('Opción inválida')
