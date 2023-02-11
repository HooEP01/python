class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


"""
my function include return a string, which is not good practise as my function name does not say that I will output string

def oldest_cat(*cats):
    cat = Cat('cat', 0)
    for item in cats:
        if item.age > cat.age:
            cat = item
    return f'The oldest cat is {cat.name}, {cat.age} years old'
"""

# Output
print(
    f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")
