found = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
print(found)
found['e'] = found['e'] + 1
print(found)
found['e'] += 1
print(found)
for i in found:
    print("{} is found {} time(s)".format(i, found[i]))
print(found)