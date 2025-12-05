# Sorting Alphabetically

# Method 1(sort a list of  tuples using sort())
def SortTuple(tup):  
    # key is set to sort using first element of  
    # sublist lambda has been used  
    # tup.sort(key = lambda x: x[0])  
    tup.sort(key=lambda x: x[0])
    return tup  
tup = [("Amana",28),
       ("Zenat", 30),
       ("Abhishek", 29),
       ("Nikhil", 21), 
       ("B",40)]    
print(SortTuple(tup))

# method 2
#sorted(iterable, key=...)
c=(sorted(tup,key=lambda x:x[0]))
print(c)