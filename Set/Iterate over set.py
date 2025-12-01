# Iterate over set

# Method 1(using loops)
a={1,2,3,4,5}
for i in a:
    print(i)

# Method 2(set.__iter__())
b = set("Vijay")
print("method 2")
for i in b.__iter__():
    print(i)

# Method 3(iter())
c=set("vardhan")
print("method 3")
for i in iter(c):
    print(i)

d = set("Uppaloju")
for idx, i in enumerate(a):
    print(idx,i)
'''enumerate() is a built-in Python function that adds a counter (index)
 to an iterable. It returns each item as a tuple containing the index 
 and the corresponding value.'''