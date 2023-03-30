from datetime import datetime
import tabula 
import csv
import glob
import pandas as pd
import os
import re

index_of_pages = 0

while index_of_pages < 56:
    df = tabula.read_pdf('./test_docs/cp/2015-2019.pdf', pages='all', area=[[122.54,36.28,329.04,259.93]])[index_of_pages]
    df.to_csv('./tests/2023_03_30-0906/'+str(index_of_pages)+'-edit-test.csv', index=False)
    with open('./tests/2023_03_30-0906/'+str(index_of_pages)+'-edit-test.csv', mode='r+') as file:
        file_readed = file.read()
        del_week_name = re.sub(r'[Ãa-z¡]', '', file_readed)
        del_letter_double_comma = re.sub(r'[A-Z],,', '',del_week_name)
        del_space_comma = re.sub(' ,', ',',del_letter_double_comma)
        del_space_line = re.sub(' - ', ',',del_space_comma)
        del_letter_number = re.sub(r'U: [0-9]', '',del_space_line)
        del_space = re.sub(r'[A-Z] ,', '-', del_letter_number)
        del_letter = re.sub(r'[A-Z]', '', del_space)
        del_letter_comma = re.sub(r'[A-Z][+]', '', del_letter)
        del_special_chars = re.sub(r'00:00', '', del_letter_comma)
        del_single_comma = re.sub(r',á', '', del_special_chars)
        del_special_comma = re.sub(r'á,', ',', del_single_comma)
        del_single_comma_space = re.sub(r'    çã,', '', del_special_comma)
        date_comma = re.sub(r'(?<=[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9])', ',', del_single_comma_space)
        del_double_comma = re.sub(r',,', ',',date_comma)
        del_double_comma_again = re.sub(r',,', ',',del_double_comma)
        del_hidden = re.sub('    §£,', '', del_double_comma_again)
        # del_hidden = re.sub(r'/\ufeff+/g', '-', del_double_comma_again)
        # newStr = del_hidden.replace('\ufeff', '\u000A')

        csv_file = open('./tests/2023_03_30-0906/all_pages.csv', mode='r+')
        csv_file.read()
        csv_file.write(del_hidden)
        csv_file.truncate()

        file.seek(0)
        file.write(del_hidden)
        file.truncate()
    
    os.remove('./tests/2023_03_30-0906/'+str(index_of_pages)+'-edit-test.csv')
    
    index_of_pages += 1