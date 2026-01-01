def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def is_strong(num):
    temp = num
    s = 0

    while temp > 0:
        digit = temp % 10
        s += factorial(digit)
        temp //= 10

    return s == num


num = int(input("Enter number: "))
if is_strong(num):
    print("Strong Number")
else:
    print("Not a Strong Number")
