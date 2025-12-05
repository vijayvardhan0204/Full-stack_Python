# Addition
# method 1
a=15
b=20
c=a+b
print("method 1 result is ",c)

# method 2
# taking input from user
a=input("enter a :")
b=input("enter b :")
c=float(a) + float(b)
print("method 2 result is ",c)
#This code takes user input as strings, converts them to floats using float(), adds them and stores the sum in res.

# method 3
# using function
def add(a,b):
    return a+b
a=10
b=6
res=add(a,b)
print("method 3 result is ",res)

# method 4
# Using lambda function(nen simple ga "lf" antunna)
# lf is 1 line function that can perform operations without defining a full function block. It is useful for short, simple calculations.
result=lambda a, b: a+b
print("method 4 result is ",result(10,9)) 

# method 5
# using operator.add
#operator module, which provides functions for various arithmetic and logical operations.
import operator
print("method 5 result is ",(operator.add(14,7)))

#method 6
# using sum()
#sum() function is commonly used to add multiple numbers in an iterable like lists or tuples.
print("method 6 result is ",sum([19,1]))