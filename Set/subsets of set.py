# subsets of set

# method 1
from itertools import combinations
s={1,2,3,4,5}
k=2
subsets=list(combinations(s,k))
print("Subsets of size", k, ":",subsets)
'''1.Combinations(s, k) function generates all possible 2-element 
subsets from the set {1, 2, 3, 4}, returning an iterator of tuples.
2.ist(combinations(s, k)) converts the iterator to a list and the 
result is printed, displaying all subsets of size 2.'''

# Method 2( bit manipulation)
s = {1, 2, 3, 4}
k = 2
s=sorted(s)
n=len(s)
res=[]
for i in range (1<<n):
    subset=[s[j] for j in range(n) if (i&(1<<j))]
    if len(subset)==k:
        res.append(subset)
print("Subsets of size", k, ":", res)