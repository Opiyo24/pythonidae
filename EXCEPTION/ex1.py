try:
    x = int(input("Enter a number: "))
    y = 10/x
    print(y)
except ZeroDivisionError:
    print("You connot divide by zero!")
except ValueError:
    print("You must enter a valid number!")
except:
    print("Something went wrong!")