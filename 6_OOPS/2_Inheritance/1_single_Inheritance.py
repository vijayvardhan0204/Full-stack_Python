class Human:
    def __init__(self,num_heart):
        self.num_heart=num_heart
        self.num_eyes=2
        self.num_nose=1
    def work(self):
        print("i can work")
    def eat(self):
        print("i can eat")
class Men(Human):
    def __init__(self,name,heart):# as Men as __init__ it cant inherit 
        super().__init__(heart)# to inherit props of Human
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):# Method overriding
        super().work()# it helps to inherit parent class work
        print("I can cook")
    def display(self):
        print(f"hi,I am {self.name} and i have {self.heart} heart")
 
male_1=Men("vijay",1)
male_1.flirt()
male_1.work()
print(male_1.num_eyes)
print(male_1.name)
male_1.display

''' Method Overriding:
When a child class (subclass) has a method with the same name as a method in the parent class,
and the child provides its own version, it is called method overriding.

👉 The child class replaces the parent’s method.'''