try:
    a=int(input("Enter number:"))
    print(10/a)
except (ValueError,ZeroDivisionError):
    print("Invalid input OR divided by zero")