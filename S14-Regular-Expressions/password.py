import re
#([A-Za-z0-9$%#@]{7,}[0-9])
pattern = re.compile(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]{8,}\d")

pwd = 'supersecret123'

test = pattern.fullmatch(pwd)

print(test)