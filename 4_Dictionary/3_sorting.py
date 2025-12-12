# Sorting by keys or values
def line():
    print("----------------------------------------------------------")

# Sorting Dictionary By Key Using sort()
d={'vijay':10,'ajay':12,'sumith':31}
mykeys=list(d.keys())
mykeys.sort()
sd={i:d[i] for i in mykeys}
print(sd)
line()


# Displaying the Keys in Sorted Order using sorted() on Keys
for i in sorted(d.keys()):
    print(i,end=" ")
print()
line()

# Sorting the dictionary by key using OrderedDict
from collections import OrderedDict
d1={'vijay':10,'ajay':12,'sumith':31}
d2=OrderedDict(sorted(d.items()))
print(d2)
line()

#Sorting the Keys Alphabetically Using Sorted on Dictionary
for i in sorted(d):
    print((i,d[i]),end=" ")
print()
line()
d3=sorted(d.items())
print(d3)