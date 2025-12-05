# Prime Number
# Method 1
""""Note: We iterate only up to the square root of n because if n has any divisor greater than its square root,
 there must also be a corresponding divisor smaller than the square root. 
 So, checking beyond sqrt(n) is unnecessary and would only waste computation."""
n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is not a prime number")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")

# Method 2
#Using flag variable
n = int(input("enter number:"))
if n <= 1:
    print(False)
else:
    is_prime = True  # Flag variable
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)

# Method 3
#Using sympy.isprime() method
from sympy import *
a1=isprime(30)
print(a1)
''''In the sympy module, 
we can test whether a given number 'n' is prime or not using sympy.
isprime() function
isprime() function from the SymPy library checks if a number is prime or not.'''

# Method4(using functions)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))
