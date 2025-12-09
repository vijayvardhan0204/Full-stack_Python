# Sample Example

try:
    a = int(input("Enter number: "))
    result = 10 / a
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
else:
    print("Result =", result)
finally:
    print("This will always run.")
