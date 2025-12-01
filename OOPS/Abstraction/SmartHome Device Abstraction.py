# SmartHome Device Abstraction

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Device):
    def turn_on(self):
        print("Light ON")

class Fan(Device):
    def turn_on(self):
        print("Fan ON")

Light().turn_on()
Fan().turn_on()
