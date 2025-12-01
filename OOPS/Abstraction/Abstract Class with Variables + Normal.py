# Abstract Class with Variables + Normal Method + Abstract Method

from abc import ABC, abstractmethod

class Bank(ABC):
    bank_name = "SBI"                 # class variable

    def __init__(self, balance):
        self.balance = balance        # instance variable

    def show_balance(self):            # normal method
        print("Balance:", self.balance)

    @abstractmethod
    def withdraw(self, amount):        # abstract method
        pass

class SavingsAccount(Bank):
    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)

acc = SavingsAccount(5000)
acc.show_balance()
acc.withdraw(1000)
