"""
RESUMEN: Vender acciones
El objetivo de esta actividad es crear un programa en el que:

    1. En primer lugar nos preguntará por consola el código de la empresa de la que queremos vender acciones, por ejemplo:
        CONSOLA: Indique el código de la empresa que quiere vender acciones
        USUARIO: REE.MC

    2. Después de contestar con el nombre de la empresa, se volverá a preguntar al usuario, en este caso el número de acciones que quiere vender:
        CONSOLA: Indique el número de acciones que quiere vender
        USUARIO: 5

        Se deberá tener en cuenta que el parámetro introducido es un número y que no puede vender más acciones de las que tiene.

    3. Con los dos datos anteriores, más la fecha actual y la acción (es una venta, no una compra), se creará un registro en un archivo
"""
import csv
import os
from datetime import date
import pandas as pd

import config.configuration


def exercice_2():
    dest_folder = config.configuration.get_dest_folder()
    directory = os.path.dirname(dest_folder)

    if not os.path.exists(directory):
        os.makedirs(directory)
        with open(dest_folder + 'transactions.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            header = ['company_name', 'shares_number', 'date', 'action']
            writer.writerow(header)
    with open(dest_folder + 'transactions.csv', 'a', encoding='UTF8', newline='') as f:
        company_name = input('Introduzca el nombre de la empresa: ')
        check = check_enough_shares(company_name, 0)
        if check[0] and check[1]:
            shares_number = -1
            while shares_number == -1:
                shares_number = input('Introduzca el número de acciones que desea vender (tiene ' + str(check[1]) + ' acciones disponibles): ')
                if not shares_number.isnumeric():
                    print('Solo son válidos valores numéricos. Inténtelo de nuevo')
                    shares_number = -1
                elif int(shares_number) > check[1]:
                    print('No dispone de tantas acciones para vender, inténtelo de nuevo')
                    shares_number = -1
            data = [company_name, shares_number, date.today(), 'sell']
            if check_enough_shares(company_name, shares_number):
                writer = csv.writer(f)
                writer.writerow(data)
                print('Perfecto, se han vendido {} de la compañía {}'.format(int(shares_number), company_name))
            else:
                print('Lo siento, no tiene tantas acciones disponibles para vender.')
        else:
            print('No tiene accioenes disponibles para vender de la compañía ' + company_name)


def check_enough_shares(company_name, shares_number):
    res = [False, 0]
    transactions = pd.read_csv(config.configuration.get_dest_folder() + 'transactions.csv')
    company_shares = transactions[transactions['company_name'] == company_name]
    buy_shares = company_shares.loc[company_shares['action'] == 'buy', 'shares_number'].sum()
    sell_shares = company_shares.loc[company_shares['action'] == 'sell', 'shares_number'].sum()
    available_shares = buy_shares - sell_shares
    if available_shares >= int(shares_number):
        res = [True, available_shares]
    return res
