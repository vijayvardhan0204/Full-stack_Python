# 1. Constructor
# A constructor is a special method that runs automatically when an object is created.
# Key Points:
# 1 .Name must be __init__()
# 2 .Used to initialize instance variables
# 3 .Called once per object

# Example:
class Student:
    def __init__(self, name):
        self.name = name
# When you create object:

s = Student("Vijay")   # constructor runs automatically

# 2. Method
# A method is a function defined inside a class.
# Types of Methods:
# 1 .Instance Method → takes self
# 2 .Class Method → takes cls, uses @classmethod
# 3 .Static Method → no self, uses @staticmethod

# Example:
class Student:
    def display(self):  # instance method
        print("Hello")

# A method is just a normal function inside a class.



# 3. Decorator
# A decorator is a special function that modifies the behavior of another function or method without changing its code.
# In OOP we mainly use:
# @classmethod
# @staticmethod
# @property

# Example:
class Student:
    @staticmethod      # decorator
    def greet():
        print("Welcome!")


# A decorator starts with @ symbol.


# Simple Example to Compare All Three
class Test:
    def __init__(self):          # Constructor
        print("Object created")

    def method1(self):           # Method
        print("This is a normal method")

    @staticmethod                # Decorator
    def fun():                  
        print("This is a static method")
t=Test()
t.method1()
t.fun()
# One-line Summary

# Constructor → runs automatically, initializes object

# Method → function inside class executed manually

# Decorator → modifies method behavior using @