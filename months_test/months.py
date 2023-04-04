import re
import pandas as pd


with open('./months_test/month.txt') as month_file:
    month_reader = month_file.readlines()
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

        txt_file = open('./months_test/output.txt', mode='r+', encoding='utf-8')
        txt_file.read()
        txt_file.write(months.replace('\n', '@').replace('@', '\t\r\n').replace('\n', '-').replace('  ', ''))
        txt_file.truncate()
        index = index + 1