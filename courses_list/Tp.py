list = [1, 7, 10, 11, 20]
listName = ['Samir', 'Taha', 'Todo']

i = 0
for name in listName:
  i = i + 1
  print(i, name)
  
print("---------------")
for i in range(len(listName)):
#  name = listName[i]
#  print(name + " you're in " + str(i))

  print(i + 1, listName[i])

print("----------Concatenation----------------")

listOne =  [1, 2, 3]
listTow =  [4, 5, 6]

listThree = listOne + listTow # [1, 2, 3, 4, 5, 6]

print(listThree)
print("---------- Slicing -----------")
print(listThree[:])
print(listThree[1:5])
print(listThree[:4])
print(listThree[5:])

print("---------- List Methods -----------")

x = [] #list
print(type(x))
#print(dir(x))

print("---------- Building a list from scratch -----------")

newList = []

newList.append("Hamza")
newList.append("Meryem")
newList.append("Salah")
newList.append("Papa")
newList.append("Mama")
print(newList)

# newList.pop()
# newList.pop()
# newList.pop()
# print(newList)

print("Hamza" in newList)
print("Hamza" not in newList)
print("Papa" in newList)

newList.sort()

print(newList)

print(len(listThree))
print(max(listThree))
print(min(listThree))
print(sum(listThree))
print(sum(listThree) / len(listThree))



