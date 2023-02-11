# debugging

# 1. linting (such as pylance)
# 2. IDE / Editor
# 3. Read errors
# 4. PDB
import pdb

def add(num1, num2):
    # debug
    print(num1, num2)
    # debug using pdb
    pdb.set_trace()
    '''
    type num1 or num2 in pdb terminator
    '''
    return num1 + num2

add(1,'2')

'''
name error
syntax error
type error
value error
key error
attribute error
15 - 20 errors show 90% of the time
'''