import difflib
import filecmp
f1 = "./test_docs/cp/all.csv"
f2 = "./test_docs/cp/already.csv"

ot = open('./out.txt', 'w')
ot.close()

# Importing difflib
  
with open(f1) as file_1:
    file_1_text = file_1.readlines()
  
with open(f2) as file_2:
    file_2_text = file_2.readlines()
  
# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile=f1, 
        tofile=f2, lineterm=''):
        txt = open('./out.txt', 'r+')
        txt.read()
        txt.write(line)
        txt.truncate()