import re

def filter_one(base):
    del_pipelines = re.sub(' | ', ',', base)
    del_pipelines_comma = re.sub(r'[ | ]', '', del_pipelines)
    fix_number_point = re.sub(r'[.][0-9]', '', del_pipelines_comma)
    del_triple_comma = re.sub(',,,', ',', fix_number_point)
    del_double_comma = re.sub(',,', ',', del_triple_comma)
    fix_month_year = re.sub(r'(?<=[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9],)', '\n', del_double_comma)
    fix_weekdays_names = re.sub(r'[A-Z][A-Z][A-Z],', '', fix_month_year)

    return fix_weekdays_names

def filter_two(base):
    del_week_name = re.sub(r'[Ãa-z¡]', '', base)
    del_letter_double_comma = re.sub(r'[A-Z],,', '', del_week_name)
    del_space_comma = re.sub(' ,', ',', del_letter_double_comma)
    del_space_line = re.sub(' - ', ',', del_space_comma)
    del_letter_number = re.sub(r'U: [0-9]', '', del_space_line)
    del_space = re.sub(r'[A-Z] ,', '-', del_letter_number)
    del_letter = re.sub(r'[A-Z]', '', del_space)
    del_letter_comma = re.sub(r'[A-Z][+]', '', del_letter)
    del_special_chars = re.sub(r'00:00', '', del_letter_comma)
    del_single_comma = re.sub(r',á', '', del_special_chars)
    del_special_comma = re.sub(r'á,', ',', del_single_comma)
    del_single_comma_space = re.sub(r'    çã,', '', del_special_comma)
    del_double_comma = re.sub(r',,', '', del_single_comma_space)
    put_comma = re.sub(r'(?<=[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9])', ',', del_double_comma)
    del_hidden = re.sub('§£', '', put_comma)
    put_comma_again = re.sub(r'(?<=[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9])', ',', del_hidden)
    del_spaces = re.sub(r'\t\n\r', '', put_comma_again)
    del_whitespaces = re.sub(" ", "", del_spaces)
    del_double_comma_again = re.sub(',,', ',', del_whitespaces)

    return del_double_comma_again

def lines_month(base, out):
    all_date = re.sub(r'(?<=[0-9][0-9]),','/'+str(out).replace('\n', ''), base)
    other = re.sub(r'(?<=:[0-9][0-9])', '|', all_date)
    ot = re.sub(r'[ | ]/[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9]', '', other)
    pipe = re.sub(r'[ | ]', '', ot)
    remove_prefix = pipe.removeprefix(',')
    months = re.sub(r'[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9]/[A-Z][A-Z][A-Z]/[0-9][0-9][0-9][0-9],', '', remove_prefix)
    replace_jan = re.sub(r'JAN','01',months)
    replace_feb = re.sub(r'FEV','02',replace_jan)
    replace_mar = re.sub(r'MAR','03',replace_feb)
    replace_apr = re.sub(r'ABR','04',replace_mar)
    replace_may = re.sub(r'MAI','05',replace_apr)
    replace_jun = re.sub(r'JUN','06',replace_may)
    replace_jul = re.sub(r'JUL','07',replace_jun)
    replace_aug = re.sub(r'AGO','08',replace_jul)
    replace_sep = re.sub(r'SET','09',replace_aug)
    replace_out = re.sub(r'OUT','10',replace_sep)
    replace_nov = re.sub(r'NOV','11',replace_out)
    replace_dec = re.sub(r'DEZ','12',replace_nov)

    return replace_dec