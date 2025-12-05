# Remove items

# Method 1(Remove())
a = {1, 2, 3, 4, 5}
a.remove(3)  
# a.remove(9) raises error as 9 is not present.
print("remove:",a)
'''a.remove(3) removes element "3" from the set a and 
if element is not found then it raises a KeyError.'''

# Method 2 (discard())
b={1,2,3,4,5}
b.discard(4)
b.discard(6) # it doesnt raise error
print("discard:",b)
'''discard(3) method removes element "3" from the set a if it exists.
discard(6) method does nothing because "6" is not present in set and no error is raised.'''

# Method 3(pop())
c={1,2,3,4,5}
r=c.pop()
print("pop:",c)
print(f"removed:{r}")
'''pop() method removes and returns a random element from the set "a" and removed element is stored in variable "r".
After removal, set "a" is printed showing remaining elements without randomly chosen item.'''


# Method 4(clear())
d = {1, 2, 3, 4, 5}
d.clear()  
print(d)
'''clear() method removes all elements from the set "a", leaving it empty.'''