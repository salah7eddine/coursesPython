readFile = open('../openFile/docs/mbox-short.txt')

for line in readFile:
  line = line.rstrip()
  if not line.startswith('From ') : continue
  arrWords = line.split()
  print(arrWords[2], arrWords[3], arrWords[6])
  arrEmail = arrWords[1].split('@') 
  
  print(arrEmail[1])