'''The __init__() Method
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.'''

# example:
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("vijay",21)
print(p1.name)
print(p1.age)
#Note: The __init__() method is called automatically every time the class is being used to create a new object.

print('-------------------------------------------------')

'''Why Use __init__()?

Without the __init__() method, you would need to set properties manually for each object:'''
class Person:
    pass
p2=Person()
p2.name="ajay"
p2.age=30
print(p2.name)
print(p2.age)

print('---------------------------------------------------')

'''Default Values in __init__()
You can also set default values for parameters in the __init__() method:'''

#Example:
class Persons:
    def __init__(self,name,age=20):
        self.name=name
        self.age=age
p3=Persons("Vijay")
p4=Persons("yash",25)
print(p3.name,p3.age)
print(p4.name,p4.age)