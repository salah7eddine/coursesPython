score = input("Enter Score: ")

try:
    scoreFloat = float(score)
except:
    print('Error, please enter numeric between 0 and 1')
    quit()


if scoreFloat >= 1.0 or scoreFloat < 0.0:
     print('Error, please enter numeric between 0 and 1')
elif scoreFloat < 0.6:
    print ('F')
elif scoreFloat < 0.7:
    print ('D')
elif scoreFloat < 0.8 :
    print ('C')
elif scoreFloat < 0.9:
    print ('B')
elif scoreFloat < 1.0:
    print ('A')

