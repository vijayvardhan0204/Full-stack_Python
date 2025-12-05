 # Payment System Abstraction

from abc import ABC,abstractmethod

class payment(ABC):
    def pay(self,amount):
        pass

class Googlepay(payment):
    def pay(self,amount):
        print(f"paid {amount} using googlepay")

class Phonepay(payment):
    def pay(self,amount):
        print(f"paid {amount} using Phonepay")

p=Googlepay()
p.pay(500)