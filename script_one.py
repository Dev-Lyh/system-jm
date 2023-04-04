from datetime import datetime
import tabula 
import csv
import glob
import pandas as pd
import os
import re

index_of_pages = 50

while index_of_pages < 55:

    y_one = 148.47
    x_one = 49.86
    y_two = 355.54
    x_two = 206.33

    df = tabula.read_pdf('./test_docs/cp/2007-2015.pdf', pages='all', area=[[y_one, x_one, y_two, x_two]])[index_of_pages]
    df.to_csv('./tests/tests_cp_2007/'+str(index_of_pages)+'-edit-test.csv', index=False)
    with open('./tests/tests_cp_2007/'+str(index_of_pages)+'-edit-test.csv', mode='r+') as file:
        file_readed = file.read()
        del_pipelines = re.sub(' | ', ',', file_readed)
        del_pipelines_comma = re.sub(r'[ | ]', '', del_pipelines)
        fix_number_point = re.sub(r'[.][0-9]', '', del_pipelines_comma)
        del_triple_comma = re.sub(',,,', ',', fix_number_point)
        del_double_comma = re.sub(',,', ',', del_triple_comma)
        fix_month_year = re.sub(r'(?<=[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9],)', '\n', del_double_comma)
        fix_weekdays_names = re.sub(r'[A-Z][A-Z][A-Z],', '', fix_month_year)

        csv_file = open('./tests/tests_cp_2007/all_pages.csv', mode='r+')
        csv_file.read()
        csv_file.write(fix_weekdays_names)
        csv_file.truncate()
    
    os.remove('./tests/tests_cp_2007/'+str(index_of_pages)+'-edit-test.csv')
    
    index_of_pages += 1

with open('./tests/tests_cp_2007/all_pages.csv') as pages_file:
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

        txt_file = open('./tests/tests_cp_2007/output.csv', mode='r+', encoding='utf-8')
        txt_file.read()
        txt_file.write(months)
        txt_file.truncate()
        index = index + 1

with open('./tests/tests_cp_2007/output.csv') as out_file:
# abrir o arquivo CSV de entrada
    # ler o conteúdo do arquivo CSV
    reader = out_file.read()

    # criar uma lista de linhas não vazias
    non_empty_rows = [row for row in reader if any(field.strip() for field in row)]

# abrir o arquivo CSV de saída
with open('./aba.csv', 'r+', newline='') as output_file:

    # escrever as linhas não vazias no arquivo CSV de saída
     output_file.readlines()
     output_file.seek(0)
     output_file.write(str(non_empty_rows))
     output_file.truncate()

