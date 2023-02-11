# custom types

from collections import Counter, defaultdict, OrderedDict
import datetime
from time import time
from array import array


li = [1,2,3,4,5,6,7,7,8,9,10,11,11]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

dictionary = defaultdict(lambda: 'Does not exist', {'a':1, 'b':2})
print(dictionary['f'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
# false
print(d2 == d)

dd = {'c': 100, 'd': 50}
dd2 = {'d': 50, 'c': 100}
# true
print(dd == dd2)


print(datetime.time(5, 42, 2))
print(datetime.date.today())


arr = array('i', [1,2,3])
print(arr[1])