# package name and file name
import shopping.shopping_cart
import shopping.more_shopping.more_shopping_cart

# here are different way of import
from shopping.shopping_cart import buy
# function will be overwritten (do not recommend)
from utility import *

# list specific functin or import whole file (recommend)
from utility import multiply, divide
from shopping.more_shopping import more_shopping_cart

print(shopping.shopping_cart.buy('apple'))

# it print __main__ because it module is main file
print(__name__)

if __name__ == '__main__':
    print('please run this')