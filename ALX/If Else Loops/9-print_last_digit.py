def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)