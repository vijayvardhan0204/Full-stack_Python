# Fibonacci series
# Method 1

n=int(input("enter number:"))
a,b=0,1
print("fibonacci series:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

# Method 2
n = int(input("Enter number of terms: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print("Fibonacci Series:", fib)

# Method 3(recurssive)

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
n = int(input("Enter number of terms: "))
print("fibonacci series:")
for i in range(n):
    print(fib(i),end=" ")

