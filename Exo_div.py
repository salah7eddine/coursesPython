aStr = input("Enter value a : ")  
bStr = input("Enter value b : ")  


try:
  a = float(aStr)
  b = float(bStr)
except:
  print('Error, please enter numeric, the values of two numbers are :', aStr, bStr)
  quit()



c= a/b 
print (c) 