try:
    a = int("abc")  # invalid conversion
except ValueError:
    print("Cannot convert string to integer!")
