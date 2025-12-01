# Hybrid Inheritance
'''Hybrid inheritance = Combination of two or more inheritance types
(like multi-level + multiple + hierarchical together).
Example structure:

    #    A
    #  / \
      B   C
       \ /
        D
Here you can see:
A → B → D → multi-level
A → C → D → multi-level
B and C both from A → hierarchical
D from B and C → multiple
So this mix = Hybrid.'''

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, course):
        Person.__init__(self, name)     # Direct call
        self.course = course

    def info(self):
        Person.info(self)
        print(f"Course: {self.course}")


class Employee(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)     # Direct call
        self.company = company

    def info(self):
        Person.info(self)
        print(f"Company: {self.company}")


class WorkingStudent(Student, Employee):
    def __init__(self, name, course, company):
        Student.__init__(self, name, course)   # Call Student constructor
        Employee.__init__(self, name, company) # Call Employee constructor

    def info(self):
        Student.info(self)
        print(f"Company: {self.company}")


ws = WorkingStudent("Vijay", "Python Full Stack", "TCS")
ws.info()
