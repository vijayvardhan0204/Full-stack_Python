'''Public Variables

Meaning: Accessible from anywhere — inside the class, outside the class, in subclasses, etc.
Access:
Direct access allowed everywhere.


Protected Variables

Meaning:
Convention that the variable should be used inside the class or subclasses only.
Important:
Python does NOT truly protect this variable — it is only a naming convention.

Access:
Allowed outside the class, but NOT recommended.


Why protected is only a convention?
In languages like Java/C++, _variable blocks access from outside.
But in Python:
_variable can still be accessed directly
Developers understand: “this is internal — don’t touch"'''


class Student:
    def __init__(self):
        self.name = "Vijay"     # public
        self._marks = 90        # protected

    def show(self):
        print(self.name, self._marks)

s = Student()
print(s.name)      # ✔ public
print(s._marks)    # ✔ works, but should be avoided
s.show()