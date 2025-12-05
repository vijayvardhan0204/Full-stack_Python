# Max of 2 num

# Method 1
# Using max()
a=7
b=5
print("method 1 result is ",max(a,b))

# Method 2
# Using ternary operator
#The ternary conditional operator is a short way to make decisions in one line.
#It checks a condition and chooses one value if it’s true, or another value if it’s false.
a=10
b=9
print("method 2 result is ",a if a>b else b)

# Method 3
# Using if-Else 
a=9
b=5
if a>b:
    print("method 3 result is ",a)
else:
     print("method 3 result is ",b)

# Method 4
# Using sort()
a=89
b=100
c=7
num=[a,b,c]
num.sort()
print("method 4 result is ",num[-1])
# 1st elements ni list ga arrange chesi ,sort function use chestunnam ,
# sort() arranges them in ascending order,then printing the last value.