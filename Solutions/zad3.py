import sys

list_arg = sys.argv[1:]
list_of_int = []
for x in list_arg:
    x = int(x)
    list_of_int.append(x)

list_of_int.sort()
print(list_of_int)
