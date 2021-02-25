# method  gives us sum, count, average
sum = 0.0
count = 0

while True:
  val = input("Enter number : ")

  if(val == 'done'): break

  try:
    valF = float(val)
  except:
    print('invalid number')
    continue

  sum = sum + valF
  count = count + 1

try:
  print(sum, count, sum/count)
except:
  print("number can't division by Zero")


#if(count != 0):
#  print(sum, count, sum/count)
#else:
#  print("you don't input any number, please!!!")


