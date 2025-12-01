# Hierarchical Inheritance
'''

👉 One parent class
👉 Multiple child classes inherit from the same parent'''

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print("Vehicle created")

    def info(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)   # calling Vehicle constructor
        self.seats = seats
        print("Car created")

    def info(self):
        super().info()            # calling Vehicle info()
        print(f"Seats: {self.seats}")


class Bike(Vehicle):
    def __init__(self, brand, cc):
        super().__init__(brand)   # calling Vehicle constructor
        self.cc = cc
        print("Bike created")

    def info(self):
        super().info()            # calling Vehicle info()
        print(f"Engine: {self.cc} cc")


# Creating objects
c = Car("Toyota", 5)
b = Bike("Yamaha", 150)

# Calling methods
c.info()
b.info()
