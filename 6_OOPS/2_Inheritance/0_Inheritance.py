class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
class student(Person):
    pass
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
x = student("Vijay", "vardhan")
x.printname()

''''Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''