# Encapsulation + Protected Variables

class Person:
    def __init__(self):
        self._age = 20    # protected

class Student(Person):
    def show(self):
        print(self._age)  # ✔ allowed inside child class


s = Student()
s.show()
print(s._age)   # ✔ but not recommended


# ✔ Protected: one underscore
# ✔ Accessible in child class
# ✔ Not truly hidden