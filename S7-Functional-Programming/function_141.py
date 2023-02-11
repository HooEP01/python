# map, filter, zip and reduce
from functools import reduce

my_list_reduce = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    # acc with be what return (which is acc + item)
    return acc + item


print(reduce(accumulator, my_list_reduce, 0))
print(my_list_reduce)


def multiply_by_2(item):
    return item * 2

# print(list(map(multiply_by_2, [1, 2, 3])))


def only_odd(item):
    return item % 2 != 0


# print(list(filter(only_odd, [1, 2, 3])))

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [100, 200, 300]
# print(list(zip(my_list, your_list, their_list)))
"""
result
[(1, 10, 100), (2, 20, 200), (3, 30, 300)]
"""
