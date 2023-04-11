import tabula
import os
import PySimpleGUI as sg
import re

index_of_pages = 0
quantity_of_pages = 151

ap = open('./output'+'/all_pages.csv', 'w')
ap.close()

while index_of_pages < quantity_of_pages:

    y_one = 191.02
    x_one = 35.63 
    y_two = 564.47 
    x_two = 231.67 

    df = tabula.read_pdf('./CP_JP.pdf', area=[[y_one,x_one,y_two, x_two]], pages='all')[index_of_pages]
    df.to_csv('./output'+'/'+str(index_of_pages) +'-edit-test.csv', index=False)
    with open('./output'+'/'+str(index_of_pages)+'-edit-test.csv', mode='r+') as file:
        file_readed = file.read()
        final_file = re.sub('INSS', '', file_readed)
        fff = re.sub(r"[0-9][0-9]/[0-9][0-9][0-9][0-9],Totais das Colunas:,,,", '', final_file)
        ffff = re.sub("M", '', fff)
        fffff = re.sub("s:", '', ffff)
        ffffff = re.sub(r'[.][0-9]', '', fffff)
        n = re.sub(r' - [A-z][A-z][A-z]', '', ffffff)
        nn = re.sub('FERIA', '', n)
        nnn = re.sub('ATEST', '', nn)
        nnnn = re.sub(r'Unnamed:[0-9]', '', nnn)
        nnnnn = re.sub(r'Unnamed: [0-9]', '', nnnn)
        t = re.sub(',,,,', ',', nnnnn)

        csv_file = open('./output/all_pages.csv', mode='r+')
        csv_file.read()
        csv_file.write(t)
        csv_file.truncate()

    os.remove('./output'+'/'+str(index_of_pages)+'-edit-test.csv')

    index_of_pages += 1
