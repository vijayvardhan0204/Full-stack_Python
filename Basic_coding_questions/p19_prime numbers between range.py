# prime numbers

a=int(input("enter number:"))
b=int(input("enter number:"))
for n in range(a, b):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
