import tabula
import os
import re
import filters
import interface
import PySimpleGUI as sg

index_of_pages = 0
quant_of_pages = 0

def read_hours_one(quantity_of_pages, path, destiny_path):

    global index_of_pages
    global quant_of_pages

    quant_of_pages = quantity_of_pages


    ap = open(destiny_path+'/all_pages.csv', 'w')
    ap.close()

    while index_of_pages < int(quantity_of_pages):
        sg.popup('Processando...', f'Páginas concluídas: {index_of_pages + 1} de {quantity_of_pages}', non_blocking=True, auto_close_duration=3, keep_on_top=False, auto_close=True, font=('Calibri', 14))

        # y_one = 148.47
        # x_one = 49.86
        # y_two = 355.54
        # x_two = 206.33

        y_one = 191.02
        x_one = 35.63 
        y_two = 564.47 
        x_two = 231.67 

        df = tabula.read_pdf(path, pages='all', area=[[y_one, x_one, y_two, x_two]], silent=True)[index_of_pages]
        df.to_csv(destiny_path+'/'+str(index_of_pages) +  '-edit-test.csv', index=False)
        with open(destiny_path+'/'+str(index_of_pages)+'-edit-test.csv', mode='r+') as file:
            file_readed = file.read()
            # final_file = filters.filter_one(file_readed)
            final_file = re.sub(r'Mês: ', '', file_readed)

            csv_file = open(destiny_path+'/all_pages.csv', mode='r+')
            csv_file.read()
            csv_file.write(final_file)
            csv_file.truncate()

        os.remove(destiny_path+'/'+str(index_of_pages)+'-edit-test.csv')

        index_of_pages += 1


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

            final_file = filters.lines_month(line, output)

            txt_file = open(name_file, mode='r+', encoding='utf-8')
            txt_file.read()
            txt_file.write(final_file)
            txt_file.truncate()
            index += 1

    os.remove(destiny_path+'/all_pages.csv')


def read_hours_two(quantity_of_pages, path, destiny_path):
    global index_of_pages
    global quant_of_pages

    quant_of_pages = quantity_of_pages

    ap = open(destiny_path+'/01 CP_CSV_Excel.csv', 'w')
    ap.close()

    while index_of_pages < int(quantity_of_pages):
        sg.popup('Processando...', f'Páginas concluídas: {index_of_pages + 1} de {quantity_of_pages}', non_blocking=True, auto_close_duration=2, keep_on_top=False, auto_close=True, font=('Calibri Bold', 14))

        if index_of_pages == 4:
            y_one = 122.54
            x_one = 36.28
            y_two = 306
            x_two = 259.93
        elif index_of_pages == 0:
            y_one = 122.54
            x_one = 36.28
            y_two = 388
            x_two = 259.93
        else:
            y_one = 122.54
            x_one = 36.28
            y_two = 345
            x_two = 259.93

        df = tabula.read_pdf(path, pages='all', area=[[y_one, x_one, y_two, x_two]], silent=True)[index_of_pages]
        df.to_csv(destiny_path+'/'+str(index_of_pages)+'-edit-test.csv', index=False)
        with open(destiny_path+'/'+str(index_of_pages)+'-edit-test.csv', mode='r+') as file:
            file_readed = file.read()
            final_file = filters.filter_two(file_readed)

            csv_file = open(destiny_path+'/01 CP_CSV_Excel.csv', mode='r+')
            csv_file.read()
            csv_file.write(final_file)
            csv_file.truncate()

        os.remove(destiny_path+'/'+str(index_of_pages)+'-edit-test.csv')

        index_of_pages += 1


interface.Interface(index_of_pages, quant_of_pages, read_hours_one, format_dates, read_hours_two)