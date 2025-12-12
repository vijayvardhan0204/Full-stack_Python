import sys

d1 = {'a': 1, 'b': 2, 'c': 3}

# Getting the size of the dictionary in bytes
size = sys.getsizeof(d1)

print(size)