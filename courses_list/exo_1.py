list = []

while True:
  inp = input("enter number : ")
  
  if(inp == 'done'): break
  
  try:
    num = float(inp)
  except:
    print("please enter a number")
    continue

  list.append(num)

average = sum(list) / len(list)

print(list)
print(sum(list))
print(len(list))
print("average :", average)

