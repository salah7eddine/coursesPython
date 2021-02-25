score = input("Enter Score: ")

try:
    scoreFloat = float(score)
except:
    print('Error, please enter numeric between 0 and 1')
    quit()


if scoreFloat < 1.0 and scoreFloat >= 0.9 :
    print ('A')
if scoreFloat < 0.9 and scoreFloat >= 0.8 :
    print ('B')
if scoreFloat < 0.8 and scoreFloat >= 0.7 :
    print ('C')
if scoreFloat < 0.7 and scoreFloat >= 0.6 :
    print ('D')
if scoreFloat < 0.6 and scoreFloat >= 0.0 :
    print ('F')
if scoreFloat >= 1.0 or scoreFloat < 0.0 :
    print('Error, please enter numeric between 0 and 1')