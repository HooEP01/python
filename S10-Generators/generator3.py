from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'total time took {t2 - t1} s')
        return result
    return wrapper


@performance
def forLoop():
    for i in range(10000000):
        i ** 2

"""
Tranfer range into list make iterable process slower
"""
@performance
def forLoopList():
    for i in list(range(10000000)):
        i ** 2

# 在座的各位都是垃圾
"""
We should use yield when we want to iterate over a sequence, 
but don't want to store the entire sequence in memory.
"""
@performance
def generator():
    for i in range(10000000):
        yield i ** 2

forLoop()
forLoopList()
generator()
