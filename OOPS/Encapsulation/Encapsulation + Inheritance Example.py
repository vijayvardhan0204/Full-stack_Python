# Encapsulation + Inheritance Example

class A:
    def __init__(self):
        self.__secret = "Hidden Data"   # private variable

    def show_secret(self):
        print(self.__secret)


class B(A):
    pass


obj = B()
obj.show_secret()   # ✔ works
# print(obj.__secret) ❌ Error — private not accessible

# ✔ Private variable stays hidden even in child class
# ✔ Only accessible through method