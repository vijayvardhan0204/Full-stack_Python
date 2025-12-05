# Set into dictionary 

# Method 1(dict.fromkeys())
a = {1, 2, 3, 4, 5}
# Converting set to dictionary
res = dict.fromkeys(a, 0)
print (res,type(res))

# method 2(Dictionary Comprehension)
#{ key_expression : value_expression  for item in iterable }
b={key:0 for key in a}
print(b)

# Method 3(loops)
c={}
for key in a:
    c[key]=0
print(type(c),c)

# Method 4(map())
d=dict(zip(a,map(lambda x:'vijay',a)))
print(type(d),d)
