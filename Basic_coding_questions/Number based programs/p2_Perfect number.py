def is_perfect(num):
    if num <= 1:
        return False

    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i

    return s == num


num = int(input("Enter number: "))
if is_perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
