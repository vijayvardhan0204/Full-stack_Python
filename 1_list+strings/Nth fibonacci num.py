# Method 1
# swapping method

def fib(n):
    a, b = 0, 1
    if n == 1:
        return 0
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b
num = int(input("Enter number: "))
print(fib(num))

# Method 2
# Using Recursive function
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
num=int(input("enter number:"))
result=fib(num)
print(result)