from datetime import datetime
import tabula 
import csv
import glob
import pandas as pd
import os
import re

index_of_pages = 0
message = ''

def read_hours():

    global index_of_pages
    global message

    ap = open('./tests/2023_03_30-0906'+'/all_pages.csv', 'w')
    ap.close()

    while index_of_pages < 97:

        y_one = 148.47
        x_one = 49.86
        y_two = 355.54
        x_two = 206.33

        df = tabula.read_pdf('./test_docs/cp/2007-2015.pdf', pages='all', area=[[y_one, x_one, y_two, x_two]])[index_of_pages]
        df.to_csv('./tests/2023_03_30-0906'+'/'+str(index_of_pages)+'-edit-test.csv', index=False)
        with open('./tests/2023_03_30-0906'+'/'+str(index_of_pages)+'-edit-test.csv', mode='r+') as file:
            file_readed = file.read()
            del_pipelines = re.sub(' | ', ',', file_readed)
            del_pipelines_comma = re.sub(r'[ | ]', '', del_pipelines)
            fix_number_point = re.sub(r'[.][0-9]', '', del_pipelines_comma)
            del_triple_comma = re.sub(',,,', ',', fix_number_point)
            del_double_comma = re.sub(',,', ',', del_triple_comma)
            fix_month_year = re.sub(r'(?<=[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9],)', '\n', del_double_comma)
            fix_weekdays_names = re.sub(r'[A-Z][A-Z][A-Z],', '', fix_month_year)

            csv_file = open('./tests/2023_03_30-0906'+'/all_pages.csv', mode='r+')
            csv_file.read()
            csv_file.write(fix_weekdays_names)
            csv_file.truncate()
        
        os.remove('./tests/2023_03_30-0906'+'/'+str(index_of_pages)+'-edit-test.csv')

        index_of_pages += 1
    
# def nf():
#     global message
#     class MV:
#         def __init__(self):
#             self._minha_variavel = 0
    
#         @property
#         def minha_variavel(self):
#             return self._minha_variavel
        
#         @minha_variavel.setter
#         def minha_variavel(self, novo_valor):
#             # chame a função que deseja executar quando a variável for modificada
#             minha_funcao(novo_valor)
#             self._minha_variavel = novo_valor

#     def minha_funcao(nv):
#         return print(nv)

#     obj = MV()
#     obj.minha_variavel = message


def format_dates(destiny_path):
    with open(destiny_path+'/all_pages.csv') as pages_file:

        name_file = destiny_path+'/00 CP_CSV_Excel.csv'

        ot = open(name_file, 'w')
        ot.close()

        month_reader = pages_file.readlines()
        global index
        global output
        index = 1
        for line in month_reader:

            if re.match(r'[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9]', line):
                output = line

            # print(str(output) + line)
            all_date = re.sub(r'(?<=[0-9][0-9]),', '/'+str(output).replace('\n', ''), line)
            other = re.sub(r'(?<=:[0-9][0-9])', '|', all_date)
            ot = re.sub(r'[ | ]/[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9]', '', other)
            pipe = re.sub(r'[ | ]', '', ot)
            remove_prefix = pipe.removeprefix(',')
            months = re.sub(r'[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9]/[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9],', '', remove_prefix)

            txt_file = open(name_file, mode='r+', encoding='utf-8')
            txt_file.read()
            txt_file.write(months)
            txt_file.truncate()
            index += 1
    
    os.remove(destiny_path+'/all_pages.csv')

# read_hours()
    
format_dates('./tests/2023_03_30-0906')