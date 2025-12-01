# A Class is like an object constructor, or a "blueprint" for creating objects.

# to create class we have to use 'class' keyword
class Myclass:
    x=5
p1 = Myclass() # p1 is object
p2 = Myclass()
p3 = Myclass()
print(p1.x)
print(p2.x)
print(p3.x)

#Note: Each object is independent and has its own copy of the class properties.