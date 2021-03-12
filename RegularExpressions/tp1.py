import re

txt = "Hello 2 friends: my name is Gone, please watch my videos with killua, Hero call us +21267666222, fin:"
number = "+91 (123) 456-7890"

# temp = re.search('He', txt)
# temp = re.findall('[0-9]+', txt)
# temp = re.findall('[0-9]+', txt)
# temp = re.findall('He.+?:', txt)

# 123-456-7890
# (123) 456-7890
# 123 456 7890
# 123.456.7890
# +91 (123) 456-7890

exp = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex = '\S+?@\S+'
email = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# temp = re.search(exp, number)
temp = re.search(regex, email)

num= '+212-616161'

tt = re.search('^\+[0-9]+', num)

print(tt)


if(temp):
  print("ok")
else:
  print("ko")
