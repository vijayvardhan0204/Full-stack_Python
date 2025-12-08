class Student:
    # CLASS VARIABLES
    school = "ABC School"          # public class variable
    _rating = 4.5                  # protected class variable
    __secret_code = "XYZ123"       # private class variable

    def __init__(self):
        # INSTANCE VARIABLES
        self.name = "Vijay"          # public
        self._marks = 90             # protected
        self.__password = "abcd123"  # private

    def show_parent(self):
        print("\nInside Parent Class:")
        print("Public Instance:", self.name)
        print("Protected Instance:", self._marks)
        print("Private Instance:", self.__password)

        print("Public Class:", Student.school)
        print("Protected Class:", Student._rating)
        print("Private Class:", Student._Student__secret_code)

class CollegeStudent(Student):
    def show_child(self):
        print("\nInside Child Class:")

        # INSTANCE VARIABLES
        print("Public Instance:", self.name)     # ✔ allowed
        print("Protected Instance:", self._marks) # ✔ allowed
        
        # print(self.__password)  # ❌ ERROR (private)
        print("Private Instance (mangled):", self._Student__password)  # ✔

        # CLASS VARIABLES
        print("Public Class:", Student.school)   # ✔ allowed
        print("Protected Class:", Student._rating)  # ✔ allowed

        # print(Student.__secret_code)  # ❌ ERROR
        print("Private Class (mangled):", Student._Student__secret_code)  # ✔

c = CollegeStudent()
c.show_parent()
print("--------------------------------------------------------------------------------------------------------------")
c.show_child()
