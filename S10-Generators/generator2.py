# iterable
# generators
# range iterating value one by one

def generator_function(num):
    for i in range(num):
        yield i**2

# for loop
# for item in generator_function(1000):
#     print(item)

# next function
generator = generator_function(100)
next(generator)
next(generator)
next(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))