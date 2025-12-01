'''self Parameter
*The self parameter is a reference to the current instance of the class.

*It is used to access properties and methods that belong to the class.

*Without self, Python would not know which object's properties you want to access.

*It does not have to be named self, you can call it whatever you like,
but it has to be the first parameter of any method in the class.
*Note: While you can use a different name, it is strongly recommended 
to use self as it is the convention in Python and makes your code more readable to others.'''


class car:
    def __init__(self,carname,carnum,carcolor):
        self.carname=carname
        self.carnum=carnum
        self.carcolor=carcolor

    def name(self):
        print("car name is "+self.carname)
obj=car("Audi",7676,"black")
obj.name()

print("--------------------------")

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("vijay", 16)
p1.greet()


'''Accessing Properties with self

You can access any property of the class using self:

Example
Access multiple properties using self:

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()


Calling Methods with self
You can also call other methods within the class using self:

Example
Call one method from another method using self:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()'''