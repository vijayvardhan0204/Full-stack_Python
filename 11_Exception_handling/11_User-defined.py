class LowBalanceError(Exception):
    pass

balance = 500
withdraw = int(input("Enter amount to withdraw: "))

try:
    if withdraw > balance:
        raise LowBalanceError("Insufficient balance!")
    balance -= withdraw
    print("Withdrawal successful. New balance:", balance)
except LowBalanceError as e:
    print("Error:", e)
