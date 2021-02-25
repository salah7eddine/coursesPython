name = "abousaid hamza"

print(type(name))
# print(dir(name))

print(name.upper())
print(name.lower())
print(name.capitalize())


print(name.find('z'))
print(name.find('y'))


print("HamZa" == "hamza")
print("HamZa".upper() == "hamza".upper())
print("HamZa".lower() == "hamza".lower())


print(name.replace('hamza', 'meryem'))


mery = "     meryem Abousaid      "

print(mery.lstrip())
print(mery.rstrip())
print(mery.strip())

print(name.startswith("H"))
print(name.startswith("ABOUSAID") or name.startswith("abousaid"))



email = "my email is abousaidMizo@gmail.com and my phone is +0000"

atPos = email.find('@')
print(atPos)

supp = email.find(' ', atPos)

res = email[atPos+1 : supp]
print(res)


print("Hello" + 'there')

