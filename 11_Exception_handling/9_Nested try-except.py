try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero inside inner block!")
except ValueError:
    print("Outer block: invalid input!")
