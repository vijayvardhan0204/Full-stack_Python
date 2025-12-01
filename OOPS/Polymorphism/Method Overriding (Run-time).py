# Method Overriding (Run-time Polymorphism)

# When a child class redefines a method of the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()


# ✔ Same method → sound()
# ✔ Different output → based on object
# ✔ This is real OOP polymorphism in Python