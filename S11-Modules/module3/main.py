# built in modules - random

import random
# import random as random

# help(random)
# print(dir(random))
print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)