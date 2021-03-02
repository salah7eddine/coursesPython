counts = dict()

# print("Enter a line of text: ")

line = input("Enter a line of text: ")


words = line.split()

for word in words:
  counts[word] = counts.get(word, 0) + 1
  print(counts)


print('Counts :', counts)

for key in counts:
  print(key, counts[key])


print(counts.keys())
print(counts.values())
print(counts.items())


# for key, value in counts.items():
#   print(key, value)


bigCount = None
bigWord = None

for key, value in counts.items():
  if bigCount is None or value > bigCount :
    bigWord = key
    bigCount = value

print('bigCount', 'bigWord')
print(bigCount, bigWord)

stuff = dict()
stuff= {'candy' : 5, 'key' : 7}
print(stuff['candy'])

