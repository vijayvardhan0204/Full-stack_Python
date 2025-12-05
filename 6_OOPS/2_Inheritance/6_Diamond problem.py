# Diamond problem
'''Diamond inheritance happens when:

👉 One base class
👉 Two classes inherit from it
👉 Another class inherits from both of them

Shapes like a diamond:

        A
       / \
      B   C
       \ /
        D


This creates a conflict:

Which version of As method should D use?

Bs? Cs? Or As?

Python solves this using 
MRO (Method Resolution Order).
C3 Linearization
single predictable path'''

class Device:
    def info(self):
        print("Device info")

class Phone(Device):
    def info(self):
        print("Phone info")
        super().info()

class Camera(Device):
    def info(self):
        print("Camera info")
        super().info()

class SmartPhone(Phone, Camera):
    def info(self):
        print("SmartPhone info")
        super().info()


sp = SmartPhone()
sp.info()
print(SmartPhone.mro())

'''What is C3 Linearization? (Simple Answer)

C3 Linearization is the algorithm Python uses to compute the MRO (Method Resolution Order) when a class has multiple inheritance (especially diamond / hybrid).

It decides which class to search first when you call a method.

👉 It guarantees:
✔ No ambiguity
✔ Consistent ordering
✔ Parents come before children
✔ Left-to-right priority (as written in class definition)'''