namesCount = dict()
names = ['Hamza', 'Hamza', 'Hamza', 'Meryem', 'Meryem', 'Papa', 'Meryem', 'Papa', 'Meryem', 'Papa', 'Meryem', 'Papa', 'Meryem', 'Papa', 'Mama', 'Papa', 'Mama', 'Papa', 'Mama', 'Papa', 'Mama', 'Papa', 'Mama', 'Papa', 'Mama', 'Papa', 'Mama']



for name in names:
   namesCount[name] = namesCount.get(name, 0) + 1

print(namesCount)

# for name in names:
#   if name not in namesCount:
#     namesCount[name] = 1
#   else :
#     namesCount[name] = namesCount[name] + 1







# print(namesCount)
# print(namesCount.get("Hamza", 0))
# # namesCount.pop()
# # print(namesCount)
# print(namesCount.keys())
# print(namesCount.values())
# print(namesCount.items())