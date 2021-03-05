nameFile = input("Enter name file : ")
if len(nameFile) < 1: nameFile = "romeo.txt"

txt = open('../openFile/docs/' + nameFile)

temp = dict()

for line in txt:
  words = line.split()
  for word in words:
    temp[word] = temp.get(word, 0) + 1

# lst = list()
# for k, v in temp.items():
#   lst.append((v, k))

# lst = sorted(lst, reverse=True)
# print(lst)

lst = sorted([(v, k) for k, v in temp.items()], reverse=True)

for val, key in lst[:5]:
  print(val, key)

tpl = tuple()

tpl = (1, 2)
print(tpl[1])
