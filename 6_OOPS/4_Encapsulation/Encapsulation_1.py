class BackAct:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def get_balance(self):
        return self.__balance

acc=BackAct()
acc.deposit(500)
print(acc.get_balance())

'''
Here:

__balance is hidden

No one can directly change it

Only methods control it → encapsulation

✅ What details are hidden?

Sensitive data (password, pin, balance, salary)

Implementation logic

Internal working of class

Only required methods are exposed

Example: Users cannot see how deposit() works internally.'''