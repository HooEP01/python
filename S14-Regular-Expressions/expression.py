import re

pattern = re.compile('this')
string = 'search this inside of this text please!'

# print('search' in string)
# = true

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.group())
print(b)
print(c)