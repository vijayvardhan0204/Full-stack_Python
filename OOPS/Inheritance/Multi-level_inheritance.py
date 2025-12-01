# Multi level inheritance
'''Multi-level inheritance means
A class inherits from another class,
and another class inherits from that class.'''

class Vehicle:
    def __init__(self,brand):
        self.brand=brand
        self.num=123
        print("Vehicle created")

    def engine(self):
        print(f"{self.brand} has a basic engine")


class Car(Vehicle):
    def __init__(self, brand, wheels):
        Vehicle.__init__(self,brand)  # calling Vehicle constructor
        # super().__init__(brand)   #calling Vehicle constructor
        self.wheel=1
        self.wheels = wheels
        print("Car created")

    def wheels_info(self):
        print(f"{self.brand} car has {self.wheels} wheels")
    
    def engine(self):
        super().engine()
        print(f"{self.brand} car engine upgraded")


class SportsCar(Car):
    def __init__(self, brand, wheels, turbo_power):
        super().__init__(brand, wheels)   # calling Car constructor
        self.turbo_power = turbo_power
        print("SportsCar created")

    def engine(self):
        super().engine()
        print(f"{self.brand} sports engine: {self.turbo_power} HP")

    def turbo(self):
        print(f"Turbo mode activated with {self.turbo_power} HP")


s = SportsCar("BMW",4,500)
s.engine()
s.wheels_info()
s.turbo()
print(s.num)
print(s.wheel)