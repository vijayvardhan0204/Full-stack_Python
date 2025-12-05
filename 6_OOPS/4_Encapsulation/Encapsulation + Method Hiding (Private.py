# Encapsulation + Method Hiding (Private Method)

class Car:
    def __init__(self):
        self.__speed = 0

    def start(self):
        self.__engine_check()
        print("Car started")

    def __engine_check(self):   # private method
        print("Engine OK")

c = Car()
c.start()
# c.__engine_check()   ❌ Error

# ✔ Method is hidden
# ✔ Outside code cannot call __engine_check()