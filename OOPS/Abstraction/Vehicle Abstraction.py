# Vehicle Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):        # abstract class
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):       # child class
    def start(self):
        print("Bike starts with kick")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

b = Bike()
b.start()

c = Car()
c.start()
