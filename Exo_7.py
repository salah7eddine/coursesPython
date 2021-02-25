largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        numF = int(num)
    except:
        print("Invalid input")
        continue

    if(smallest is None and largest is None):
        smallest = numF
        largest = numF
    


    if(smallest > numF):
        smallest = numF
    
    if(largest < numF):
        largest = numF
        

print("Maximum is", largest)
print("Minimum is", smallest)