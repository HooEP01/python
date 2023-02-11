# print module name
print(__name__)
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return 'error'