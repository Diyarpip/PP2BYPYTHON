class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False


balance, withdrawal = map(int, input().split())


acc = Account(balance)


if acc.withdraw(withdrawal):
    print(acc.balance)
else:
    print("Insufficient Funds")