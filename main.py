import pandas as pd
import tabula
import re
import json
from datetime import datetime

# Getting the current date and time
ts = datetime.now().strftime("%Y_%m_%dT%H-%M-%S")
filename = './' + ts + '.json'

list_tables = tabula.read_pdf(input_path="./test_docs/cp/2015-2019.pdf", pages="all", output_path='./outputFile.json', area=[[122.54,36.28,329.04,259.93]], stream=True, guess=False)
#print(list_tables)

f = open('./outputFile.json')
data = json.load(f)
data_to_string = json.dumps(data)
hours_alone = re.findall(r'[0-9][0-9]:[0-9][0-9] [0-9][0-9]:[0-9][0-9]' and r'[0-9][0-9]:[0-9][0-9]', data_to_string)
hours_together = "".join(hours_alone)
# hours_together_2 = hours_together.split('-',-4)
upper_then = re.sub(r'(?<=1[5-9]:\d\d)','\r\n', hours_together)
less_then = re.sub(r'(?=1[0-9]:\d\d)|(?=0[0-9]:\d\d)|(?=1[1-6]:\d\d)|(?=2[0-3]:\d\d)',',', upper_then)

file = open('CP.csv', 'a')
file.write(less_then)
file.close()

print(less_then)

# top 17.11mm -> 48.50 Y1
# left 38.20mm -> 108.28 X1
# width 84.24mm -> 238.79 
# height 267.13mm -> 757.21
# top + height = 279,75mm -> 805.71 Y2
# left + width = 171,65mm -> 307.07 X2
# 48.50,108.28,805.71,307.07

# top 12.80mm -> 36.28 pt Y1
# left 86.24mm -> 244.45 X1
# width 84.24mm -> 238.79 
# height 267.13mm -> 757.21
# top + height = 279.75mm -> 792.99 Y2
# left + width = 171.65mm -> 486.56 X2
# 36.28,244.45,792.99,486.56
#122.54