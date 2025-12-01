# Adding tuple to list and vice versa
# method 1
a = [1, 2, 3] 
b = (4, 5)    
c = [6, 7]    
# add tuple to list a
a.extend(b) 
print("using extend:",a)
# add list to tuple b
d = b + tuple(c)
print("using + :",d)
'''' extend() adds each element individually to a list, 
while + concatenates sequences.'''

# method 2
x = [1, 2, 3] 
y = (4, 5) 
z = [6, 7] 
# add tuple to list a
x.append(y)
print("using append:",x)
# add list to tuple b
f = (*y, *z)
print("using * :",f)
''''append() adds the entire tuple as a single element.
 The * operator unpacks elements for merging sequences.'''

# method 3
i = [1, 2, 3]
j = (4, 5)
k = [6, 7] 
# add tuple to list a
i.insert(len(i), j)
print("using insert:",i)
# add list to tuple b
l = tuple(a for a in j) + tuple(k)
print("using list comprehension:",l)

# method 4

g = [1, 2, 3]
h = (4, 5) 
m = [6, 7] 
# add tuple to list a
g.extend(list(h))
print("using list():",g)
# add list to tuple b
temp_list = list(h)
temp_list.extend(m)
n = tuple(temp_list)
print("using tuple():",n)