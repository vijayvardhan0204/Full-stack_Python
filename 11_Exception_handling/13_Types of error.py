print("----- Demonstrating All Major Errors in One Code -----")

# 1. NameError
try:
    print(x)          # x not defined
except NameError as e:
    print("NameError:", e)


# 2. ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)


# 3. ValueError
try:
    num = int("abc")
except ValueError as e:
    print("ValueError:", e)


# 4. TypeError
try:
    print("hello" + 5)   # strings + int not allowed
except TypeError as e:
    print("TypeError:", e)


# 5. IndexError
try:
    a = [1, 2, 3]
    print(a[5])
except IndexError as e:
    print("IndexError:", e)


# 6. KeyError
try:
    d = {"name": "Vijay"}
    print(d["age"])
except KeyError as e:
    print("KeyError:", e)


# 7. FileNotFoundError
try:
    open("abc.txt", "r")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)


# 8. AttributeError
try:
    x = 10
    x.append(5)
except AttributeError as e:
    print("AttributeError:", e)


# 9. ImportError
try:
    import mymodule   # module does not exist
except ImportError as e:
    print("ImportError:", e)


# 10. IndentationError (Cannot execute in code)
print("\nIndentationError cannot be shown at runtime because:")
print("It stops the program BEFORE running.")
print("But example is: \nfor i in range(5):\nprint(i)")


print("\n----- End of Error Demonstration -----")
