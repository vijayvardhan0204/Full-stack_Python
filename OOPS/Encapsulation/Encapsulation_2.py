class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, amount):
        if amount > 1000:
            self.__salary = amount
        else:
            print("Invalid salary")

    def get_salary(self):
        return self.__salary


e = Employee()
e.set_salary(500)    # Invalid
e.set_salary(30000)  # Valid
print(e.get_salary())


# ✔ You control how data is changed
# ✔ Direct access is blocked