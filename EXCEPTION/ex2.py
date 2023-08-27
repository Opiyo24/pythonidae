try:
    f = open("file.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
finally:
    f.close()