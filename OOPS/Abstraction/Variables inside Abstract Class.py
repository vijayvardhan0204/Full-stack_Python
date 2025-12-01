# Variables inside Abstract Class

from abc import ABC, abstractmethod

class Car(ABC):
    wheels = 4              # class variable
    def __init__(self, brand):
        self.brand = brand  # instance variable

    @abstractmethod
    def start(self):
        pass

class BMW(Car):
    def start(self):
        print(f"{self.brand} starts with a button. It has {self.wheels} wheels.")

b = BMW("BMW X7")
b.start()
