# Multiple Inheritance
# one child class but 2 parent classes,it inherits the properties of both the parent classes

class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male:
    def __init__(self,name):
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code")
class boy(Human,Male):
    def __init__(self,name,num_heart,language):
        Male.__init__(self,name)
        Human.__init__(self,num_heart)
        self.language=language
    def sleep(self):
        print("i can sleep")
    def work(self):
        print("i can test")
boy_1=boy("vijay",1,"python")
boy_1.work()#i can work because 1st Human props are inheriting
Male.work(boy_1)
print(boy.mro()) #1st priority is given to boy
#Method resolution order

print(boy_1.num_eyes)
print(boy_1.num_heart)
print(boy_1.language)