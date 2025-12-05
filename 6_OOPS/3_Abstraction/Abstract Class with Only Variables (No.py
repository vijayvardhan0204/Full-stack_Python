# Abstract Class with Only Variables (No Abstract Method)

from abc import ABC

class Device(ABC):
    name = "Smart Device"
    version = 1.0

class Phone(Device):
    pass

print(Phone.name)
print(Phone.version)
