# Set to String

# Method 1(str)
a = {1, 2, 3}
res = str(a)  # direct conversion
print(type(res), res)

# Method 2(f-string)
b=f"{a}"
print(type(b),b)
'''f-strings (f"{a}") offer a simple and readable way to convert 
a set to a string. They directly format the set as a string, 
maintaining its curly braces. 
This method is useful when quick and concise formatting is needed.
'''

# method 3(repr())
c=repr(a)
print(type(c),c)
'''repr() function provides an official string representation of the set,
 including curly braces {}. 
 This method is best suited for debugging and logging purposes 
 since it ensures an exact representation of the set.'''

# Method 4(join())
rest=" ,".join(map(str,a))
print(type(rest),rest)
'''map(str, s) converts each element in the set to a string.
join() merges all the converted strings into a single string, separated by ','.'''