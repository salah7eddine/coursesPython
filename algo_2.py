# algo to find number

def findPairNumber(num):
  print(num)
  if(num % 2 == 0):
    print('pair')
  if(num % 2 == 1):
    print('impair')


def findPairNumberV2(num):
  print(num)
  if(num % 2 == 0):
    print('pair')
  else:
    print('impair')


def add(a, b):
  return a + b

def mince(a, b):
  return a- b



print(add(10, 45))
print(mince(17, 54))
#findPairNumberV2(13)

def positiveOrNegative(num):
  if(num > 0):
    print(str(num) + ' positive')
  if(num < 0):
    print(str(num) + ' negative')


#positiveOrNegative(-7)

#positiveOrNegative(17)



# findPairNumber(23)

#for i in range(20):
#  findPairNumber(i)

