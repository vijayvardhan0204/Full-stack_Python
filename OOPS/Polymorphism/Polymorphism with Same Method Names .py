# Polymorphism with Same Method Names (Duck Typing)

# Even without inheritance, if different classes have the same method, Python allows calling them in a loop.

class Car:
    def start(self):
        print("Car starts with key")

class Bike:
    def start(self):
        print("Bike starts with kick")

for v in (Car(), Bike()):
    v.start()


# ✔ Python only checks if method exists
# ✔ Class type doesn’t matter
# ✔ This is duck typing polymorphism