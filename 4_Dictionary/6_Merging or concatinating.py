# Merging or concatinating

# Method 1(Using | operator)
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1 | d2
print(d3)

# Method 2(Dictionary Unpacking (**))
d4={**d1,**d2}
print(d4)

# Method 3 (update())
d1.update(d2)
print(d1)

# Method 4
d5={'name':'vijay','age':20}
d6={'age':21,'roll':'R3'}
d7=d5.copy()
for key,value in d6.items():
    d7[key]=value
print(d7)