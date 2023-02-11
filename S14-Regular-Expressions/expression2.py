import re

pattern = re.compile(r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
string = 'Hoo Ern Ping'
string2 = 'email@email.com'
a = pattern.search(string)
b = pattern.search(string2)
print('a', a)
print('b', b)