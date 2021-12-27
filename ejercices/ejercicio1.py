"""
RESUMEN: Comprar acciones
El objetivo de esta actividad es crear un programa en el que:

    1. En primer lugar nos preguntará por consola el código de la empresa de la que queremos comprar acciones, por ejemplo:
        CONSOLA: Indique el código de la empresa que quiere comprar acciones
        USUARIO: REE.MC

    2. Después de contestar con el nombre de la empresa, se volverá a preguntar al usuario, en este caso el número de acciones que quiere comprar:
        CONSOLA: Indique el número de acciones que quiere comprar
        USUARIO: 5

        Se deberá tener en cuenta que el parámetro introducido es un número.

    3. Con los dos datos anteriores, más la fecha actual y la acción (es una compra, no una venta), se creará un registro en un archivo
"""
import csv
import os
from datetime import date

import config.configuration


def exercice_1():
    dest_folder = config.configuration.get_dest_folder()

    repeat = True

    while repeat:
        company_name = input('Introduzca el nombre de la empresa: ')

        if config.configuration.check_company_in_market(company_name):
            shares_number = -1
            while shares_number == -1:
                shares_number = input('Introduzca el número de acciones que desea comprar: ')
                if not shares_number.isnumeric():
                    print('Solo son válidos valores numéricos. Inténtelo de nuevo')
                    shares_number = -1
            directory = os.path.dirname(dest_folder)
            data = [company_name, shares_number, date.today(),'buy']
            if not os.path.exists(directory):
                os.makedirs(directory)
                with open(dest_folder + 'transactions.csv', 'w', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    header = ['company_name', 'shares_number', 'date', 'action']
                    writer.writerow(header)
            with open(dest_folder + 'transactions.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
                print('Perfecto, se han comprado {} de la compañía {}'.format(int(shares_number), company_name))
                repeat = False
        else:
            ask = input('Lo sentimos, no existe ninguna compañía con ese nombre. Si desea volver a intentarlo pulse "s", cualquier otra tecla en caso contrario\nDecisión: ')
            if ask != 's':
                repeat = False
