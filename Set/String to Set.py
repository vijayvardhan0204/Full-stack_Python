# String to Set

# Method 1(set) 
s="vijay"
set_s=set(s)
print(type(set_s),set_s)

# Method 2(set() with split() for words)
v= "python is not too complex"
set_words=set(v.split())
print(type(set_words),set_words)

# method 3(dict.fromkeys())

set_w=set(dict.fromkeys(s))
print(type(set_w),set_w)
'''using dict.fromkeys() as it creates a dictionary from an iterable 
and sets the values to none for every key.'''