# set into a list


# Method 1(list constuctor)
a = {1, 2, 3, 4, 5}
b = list(a)
print(b)

# Method 2(List comprehension)
c=[i for i in a]
print(c)

# Method 3(unpacking)
d=[*a]
print(d)

# MEthod 4(append())
e=[]
for i in a:
    e.append(i)
print(e)

# Method 5
f=list(map(lambda x:x, a))#lambda parameters: expression, map(function ,iterable)
print(f)

#Method 6(copy() Method (Shallow Copy of Set to List))
g=a.copy()
print(g)
'''The copy creates a new set, then converting to a list makes a new list,
 but all elements (numbers) are the same objects'''

# Method 7(extend())
h=[]
h.append(a)
print(h)
