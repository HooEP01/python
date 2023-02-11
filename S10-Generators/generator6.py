# Fibonacci number
"""
The Fibonacci sequence begins with the following 14 integers: 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ... Each number, 
starting with the third, adheres to the prescribed formula. 

For example, the seventh number, 8, is preceded by 3 and 5, which add up to 8.
"""

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a 
        temp = a
        a = b
        b = temp + b


def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


for x in fib(20):
    print(x)

print(fib2(1000))