import re

nameFile = input('Enter the name of the file : ')
if len(nameFile) < 1: nameFile = "regex_sum_1162447.txt"

handle = open('data/' + nameFile)

lst = list()

for line in handle:
  numStr = re.findall('[0-9]+', line)
  if(len(numStr) == 0): continue

  for itrNum in numStr:
    print(itrNum)
    num = int(itrNum)
    lst.append(num)
    
print(len(lst), sum(lst))