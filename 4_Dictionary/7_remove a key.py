# remove a key from dictionary

# Method 1(using pop())
a = {"name": "Vijay", "age": 21, "city": "Hyderabad"}
rv = a.pop("age")
print(a)  
print(rv)

# Method 2(del())
del a["city"]
print (a)

# Method 3
b = {"name": "Nikki", "age": 25, "city": "New York"}
c = b.popitem()
print(b)  
print(c)