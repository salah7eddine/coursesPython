# D-R-Y :: don't repeat yourself

def hello():
  print("body")
  print("Hello world")


#hello()

def name(name):
  print("My name is " + name)

def sum(a, b, c):
  return a + b + c

def add(a, b):
  return a + b

def add(a, b):
  print(str(a) + " + " + str(b))

def add(a, b):
  print(a + b)

#c = add(10, 10)
#d = sum(10, 10, 10)

#print(c, d)


#charMax = max("Hamza Abousaid")
#charMin = min("Hamza Abousaid")
charMax = max("Abcdef")
charMin = min("Abcdef")

#print(charMax, charMin)



## lang


def say(lang):
  if(lang == "es"):
    print("Holla")
  elif(lang == "fr"):
    print('bonjour')
  elif(lang == "tu"):
    print("Salam in Turkie")
  else:
    print("Salam")

say("fr")
say("es")
say("ar")
say("tekherbi9a")



# Return Value
def greet(lang):
  if lang == "es":
    return "Hola"
  elif lang == "fr":
    return "Bonjour"
  else:
    return "Hello"


print(greet("es"), "Hamza")
print(greet("en"), "Hamza")
print(greet("fr"), "Hamza")




def meth():
  print('body')


