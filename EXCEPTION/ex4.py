'''
You can use the from keyword with raise to specify another exception as the cause of your execption
This can help preserve the original context of the error
and provide more infiormation to the user or debugger
'''

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ValueError("Invalid arguments!") from e

try:
    z = divide(10, 0)
    print(z)
except ValueError as e:
    print(e)
    print(e.__cause__)