# Factorial
# Method 1
n=int(input("enter num:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("result of method 1:",fact)

# Method 2
#Using a Recursive Approach
def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)
n=6
print("result of Recursive Approach:",fact(n))

# Method 3
# Using math.factorial()
import math
def facto(n):
    return(math.factorial(n))
n=5
print("result of math.factorial():",facto(n))

# Method 4
import numpy
n=5
x=numpy.prod([i for i in range(1,n+1)])
print("result of numpy.prod:",x)
"""This Python code calculates the factorial of n using NumPy. 
It creates a list of numbers from 1 to n, computes their product with numpy.prod(), 
and prints the result."""