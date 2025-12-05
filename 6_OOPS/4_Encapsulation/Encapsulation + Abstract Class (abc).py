# Encapsulation + Abstract Class (abc)

from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self):
        self.__color="Red" #private
    def get_color(self):
        return self.__color
    def area(self):  # abstract method
        pass

class circle(shape):
    def area(self,r):
        return 3.14*r*r
c=circle()
print(c.area(5))
print(c.get_color())

# ✔ Private variable inside abstract class
# ✔ Accessible only through getter method
# ✔ Child class cannot touch __color directly