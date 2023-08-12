# Creating a dictinary
Dict = {"Name": "Geeks  for Oporo", 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# Accessinga n element using a key
print("Accessing an element using a key: ")
print(Dict["Name"])

# Accessing an element using get() method
print("Accessing an element using get: ")
print(Dict.get(1))

# Creation using dictionary comprehension
myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)