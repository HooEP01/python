# Decorator pattern

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {(t2-t1) * 100} ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('*******')
#         func(*args, **kwargs)
#         print('*******')
#     return wrap_func


# @my_decorator
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)


# hello2 = my_decorator(hello)
# hello2()


# hello('hello')
