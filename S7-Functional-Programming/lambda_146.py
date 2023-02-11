print(list(map(lambda item: item * 2, [1, 2, 3, 4])))
print(list(filter(lambda item: item % 2 != 0, [1, 2, 3, 4, 5, 6])))

my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
