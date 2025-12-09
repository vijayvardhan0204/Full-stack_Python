# Sample Example

try:
    a = int(input("Enter number: "))
    print(10 / a)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input!")
else:
    print("Successful execution!")
finally:
    print("Program ended.")
