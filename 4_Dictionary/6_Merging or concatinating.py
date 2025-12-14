# Merging or concatinating

# Method 1(Using | operator)
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1 | d2
print(d3)

# Method 2(Dictionary Unpacking (**))
d4={**d1,**d2}
print(d4)