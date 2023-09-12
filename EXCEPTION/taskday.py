def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Cannot divide by zero!')
    else:
        print(f'The result is: {result}')
    finally:
        print('Printing the finally clause')
        return

divide('2', '0')