

list = [7, 2, 11, 20, 45, 17, 35, 1, 3]

#count = 0
#sum = 0
#for i in list:
#  count = count + 1
#  sum = sum + i
#  print(i, count, sum)

#print(count, sum)


#print("Moy", sum / count)


#for i in list:
#  if(i < 10):
#    print('smaller than 10', i)


#found = False
#for i in list:
#  if(i == 7):
#    found = True
#    print(found, i)  

#if(found):
#  print("7 exist in the list")



arr = [7, 2, 11, 20, 45, 17, 35, 1, 3]

max = -1
min = None

for i in arr:
  if(min is None): # is isNot    '7' is 7 => false
    min = i

  if(i < min):
    min = i

  if(i > max):
    max = i
  
  print(max, min, i) 

print("Max", max)
print("Min", min)





