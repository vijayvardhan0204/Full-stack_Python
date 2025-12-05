from abc import ABC,abstractmethod

class Animal(ABC):
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("barks")

class Cat(Animal):
    def sound(self):
        print("Meow")

Dog().sound()  # Bark
Cat().sound()  # Meow