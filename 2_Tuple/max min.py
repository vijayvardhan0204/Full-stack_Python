# max min

# method 1
tuple=(4,5,2,88,1)
s=list(tuple)
print("method 1")
print(max(s))
print(min(s))

# method 2

tuple=(4,5,2,88,1)
temp=sorted(tuple)
mi=temp[:1]
ma=temp[-1:]
print("method 2")
print(mi)
print(ma)

# method 3

import heapq
tup = (5, 20, 3, 7, 6, 8)
K = 2
s = heapq.nsmallest(K, tup)
l = heapq.nlargest(K, tup)
print(s)
print(l)
''''heapq.nsmallest(K, iterable): Returns the K smallest elements from the iterable.
heapq.nlargest(K, iterable): Returns the K largest elements from the iterable.'''