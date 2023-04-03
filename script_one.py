from datetime import datetime
import tabula 
import csv
import glob
import pandas as pd
import os
import re

index_of_pages = 50

while index_of_pages < 97:

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
        fix_weekdays_names = re.sub('', '', fix_month_year)

        # print(fix_weekdays_names)

        csv_file = open('./tests/tests_cp_2007/all_pages.csv', mode='r+')
        csv_file.read()
        csv_file.write(fix_month_year)
        csv_file.truncate()

        file.seek(0)
        file.write(fix_month_year)
        file.truncate()
    
    os.remove('./tests/tests_cp_2007/'+str(index_of_pages)+'-edit-test.csv')
    
    index_of_pages += 1