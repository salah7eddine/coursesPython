hrs = input("Enter Hours:")
rate = input("Enter rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

print(h, r)

if ( h <= 40 ):
    result = h * r
else :
    result = 40 * r + (h - 40) * r * 1.5
print(result)
