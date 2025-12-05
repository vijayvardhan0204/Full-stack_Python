'''abc = Abstract Base Classes module.

It is a built-in Python module used to create:

Abstract Classes

Abstract Methods'''

from abc import ABC, abstractmethod

class Car(ABC):            # abstract class
    @abstractmethod
    def speed(self):       # abstract method
        pass

class BMW(Car):            # child class
    def speed(self):
        print("BMW speed is 200 km/h")

obj = BMW()
obj.speed()

'''Car → abstract class

Contains an abstract method speed() → no body
Because we don’t know how different cars implement speed.

BMW → subclass

Gives real implementation of speed().
We cannot create object of abstract class:
Car()   # ❌ Error


Only subclass objects can be created.'''