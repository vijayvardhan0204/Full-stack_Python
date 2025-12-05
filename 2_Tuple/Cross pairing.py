# Cross pairing

''''Input : test_list1 = [(1, 7), (6, 7), (8, 100), (4, 21)], test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)] 
Output : [(7, 3)] 
Explanation : 1 occurs as tuple element at pos. 1 in both tuple, its 2nd elements are paired and returned.

Input : test_list1 = [(10, 7), (6, 7), (8, 100), (4, 21)], test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)] 
Output : [] 
Explanation : NO pairing possible.'''
# Method 1(Using list comprehension)
t1=[(1, 7), (6, 7), (9, 100), (4, 21)]
t2=[(1, 3), (2, 1), (9, 7), (2, 17)]
res=[(i1[1],i2[1]) for i1 in t1 for i2 in t2 if i1[0]==i2[0]]
print(res)

# Method 2(Using zip() + list comprehension)
rest=[(a[1],b[1]) for a,b in zip(t1,t2) if a[0]==b[0]]
print(rest)