'''Write a program that takes two numbers as
 input and calculates their division.
 Handle the ZeroDivisionError and ValueError 
 exceptions gracefully.'''

try:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("please enter another number: "))
    divide = num1 / num2
    print("The answer is: {:.0f}".format(divide))
except ValueError:
    print("ERROR: Please enter a valid number.")
except:
    if num1 < 0 or num2 < 0:
        print("ERROR: Cannot divide 0s.")
    else:
        print("An unknown error occured.")