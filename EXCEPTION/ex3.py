'''
To raise yoiur own eexceptions, you can use the raise statement.
You can pass an exception objec or an exception class as an argument to raise.
You can also provide an optional message or additional information with the exception.
'''

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise PermissionError("You are not old enough!", age)

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("You are allowed to enter!")
except PermissionError as e:
    print(e.args[0])
    print(f"You need to wait {18 - e.args[1]} years.")
except ValueError as e:
    print(e)