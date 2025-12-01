# Flatten tuple of List to tuple
''''Input: ([5, 6], [6, 7, 8, 9], [3])
Output: (5, 6, 6, 7, 8, 9, 3)'''

# Method 1
from itertools import chain
tup = ([5, 6], [6, 7, 8, 9], [3])
res=tuple(chain.from_iterable(tup))
print(res)
'''chain.from_iterable() combines multiple inner lists into a single 
sequence without creating intermediate lists. 

chain.from_iterable(tup) iterates through each sublist inside tup and extracts their elements in sequence.
tuple() converts the flattened sequence into a tuple.'''

# Method 2
rep=tuple(x for sublist in tup for x in sublist)
print(rep)
'''for sublist in tup loops through each inner list.
for x in sublist accesses each element inside the sublist.
x extracts individual elements.
tuple() converts the flat sequence into a tuple.'''

# Method 3
rest=tuple(sum(tup,[]))
print(rest)
'''sum(tup, []) means:
Start with an empty list,
and then add each list inside tup to it.'''