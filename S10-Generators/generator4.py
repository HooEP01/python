# under the hood of generators

def special_for(iterable):
    # iter iterating list one by one using 'next' function
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
            
        except StopIteration:
            break

special_for([1,2,3,4,5])