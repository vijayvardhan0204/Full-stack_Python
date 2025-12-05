# Set into Tuple and Tuple into Set

# Method(1 to 3)-> Set to tuple
'''Input: {'a', 'b', 'c', 'd', 'e'}
Output: ('a', 'c', 'b', 'e', 'd')
Explanation: converting Set to tuple

Input: ('x', 'y', 'z')
Output: {'z', 'x', 'y'}
Explanation: Converting tuple to set'''
# Method 1(Using tuple())
s = {'a', 'b', 'c', 'd', 'e'}
t=tuple(s)
print(type(t),t)

# Method 2(list comprehension)
v = {'a', 'b', 'c', 'd', 'e'} 
x=[i for i in v]
print(tuple(x))

# Method 3(enumerate)
y={'a', 'b', 'c', 'd', 'e'}
a=[j for i,j in enumerate(y)]#enumerate returns index value associated with item'
print(tuple(a))

# Method 4(set())
b=('x','y','z')
su=set(b)
print(type(su),su)

# Method 5('*' operator )*' operator can be used to unpack the elements of a set into a tuple.
test_set = {6, 3, 7, 1, 2, 4}
test_tuple=(*test_set,)
print(test_tuple)
'''*test_set = unpacking the set
It takes each item from the set and puts it individually.
Then the surrounding parentheses ( ... , ) pack the unpacked 
values into a tuple

Parentheses () alone do NOT create a tuple.
A comma creates a tuple.

Example:
x = (10)
print(type(x))

<class 'int'>

so comma(,) must be present at the end of tuple
'''
# Method 5()
c = {'a', 'b', 'c', 'd', 'e'}
tupleee=tuple()
for i in c:
    tupleee+=(i,)
print(tupleee)

# Method 6(itertools)
import itertools
sp = {'a', 'b', 'c', 'd', 'e'}
tu = tuple(itertools.chain(s))
# print the resulting tuple
print(tu)