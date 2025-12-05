# Descending order

# Method 1(sorted)
a = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]
res=sorted(a,key=lambda i:(-i[0],i[1]))
print(res)
''''sorted(a, key=lambda x: (-x[0], x[1])) sorts the list of tuples a
 by the first element in descending order and if two tuples have the
same first element, by the second element in ascending order.'''

# Method 2
a.sort(key=lambda x:(-x[0],x[1]))
print(a)
''''a.sort(key=lambda x: (-x[0], x[1])) sorts the list of tuples a in 
place by the first element in descending order and if two tuples have 
the same first element, by the second element in ascending order. 
Unlike sorted(), sort() modifies the original list.'''