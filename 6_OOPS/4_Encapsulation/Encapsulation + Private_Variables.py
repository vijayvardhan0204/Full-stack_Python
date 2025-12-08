class Student:
    __class_secret="I am CLASS level"  # private class variable

    def __init__(self,name):
        self.name=name
        self.__password="1234abcd"     # private Instance variable

    def show_instance_secret(self):
        print("Instance secret:",self.__password)

    @classmethod
    def show_class_secret(cls):
        print("class secret:",cls.__class_secret)

s = Student("Vijay")

s.show_instance_secret()
print(s._Student__password)     # works (name-mangled)

s.show_class_secret()
print(Student._Student__class_secret)   # works (name-mangled)

# WRONG: instance cannot access class variable directly
# print(s.__class_secret)         # ERROR

# #  WRONG: class cannot access instance variable
# print(Student._Student__password)   # ERROR