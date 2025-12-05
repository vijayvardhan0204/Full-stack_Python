'''Class Methods
Methods are functions that belong to a class. They define the behavior of objects created from the class.'''
# Note: All methods must have self as the first parameter.
class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"hello {self.name}")
p1=person("vijay")
p1.greet()
print("-----------------------------------------------")

'''Methods with Parameters
Methods can accept parameters just like regular functions:'''
class calculator:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
calc=calculator()
print(calc.add(1,10))
print(calc.multiply(2,30))
print("---------------------------------------------------------")

'''The __str__() Method
The __str__() method is a special method that controls what is 
returned when the object is printed:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"
# without __str__ we will get <__main__.Person object at 0x15039e602100> as output
p1 = Person("vardhan", 21)
print(p1)