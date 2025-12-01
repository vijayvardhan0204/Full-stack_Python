#find tuples which have all elements divisible by K from a list of tuples

# Method 1
# Using list comprehension + all()
test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21),(18,24,30)]
k=6
# all() used to filter elements
res=[sub for sub in test_list if all(ele % k==0 for ele in sub)]
print(res)
''''6 % 6 == 0 → True  
24 % 6 == 0 → True  
12 % 6 == 0 → True  
All are True → all(...) returns True
'''

# Method 2
#Using filter() + lambda + all()
rest = list(filter(lambda sub: all(ele % k == 0 for ele in sub), test_list))
print(rest)
''''The program uses the filter() function to filter the tuples 
in test_list based on the condition that all elements in the tuple 
are divisible by K.

filter(function, iterable)
The filter() function always needs two things:
A function → decides which items to keep
An iterable (list/tuple/string/etc.) → the items to check'''

''''A lambda in Python is a small, anonymous (nameless) function.
It is used when you need a function for a short time and 
don’t want to write a full def function.'''

# Method 3
# Using loops
resto=[]
for i in test_list:
    c=0
    for j in i:
        if j%k==0:
            c+=1
    if(c==len(i)):
        resto.append(i)
print(resto)