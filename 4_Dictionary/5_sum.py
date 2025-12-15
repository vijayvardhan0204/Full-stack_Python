# sum

# Method 1(using sum())
d = {'a': 100, 'b': 200, 'c': 300}
res = sum(d.values())
print(res)

# Method 2(loop)
res=0
for value in d.values():
    res+=value
print(res)