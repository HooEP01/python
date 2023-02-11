"""
Object oriented programming
> modeling real world object

Procedural programming
> step by step procedure to do things
"""

# All object built by class
print(type('string'))
print(type(1))
print(type((1.1)))
print(type(True))
print(type(None))
print(type([1, 2, 3]))
print(type({'name': 'Hello', 'age': 10}))
print(type({1, 2, 3}))
print(type((1, 2, 3)))

"""
Output will show like below:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
<class 'list'>
<class 'dict'>
<class 'set'>
<class 'tuple'>
"""

# We create a class or Blue Print
class BigObject:
    pass

# Create new object by intantiate a class
obj1 = BigObject()
print(type(obj1))

"""
Output will show like below:
<class '__main__.BigObject'>
"""
