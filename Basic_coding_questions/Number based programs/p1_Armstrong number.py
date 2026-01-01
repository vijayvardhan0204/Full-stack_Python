def is_armstrong(num):
    temp = num
    n = len(str(num))
    s = 0

    while temp > 0:
        digit = temp % 10
        s += digit ** n
        temp //= 10

    return s == num


num = int(input("Enter number: "))
if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
