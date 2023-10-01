class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.minWithdraw = 100
        self.maxWithdraw = 100000

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.minWithdraw:
            # return f'fokira you can not withdraw below {self.minWithdraw}'
            print(f'fokira you can not withdraw below {self.minWithdraw}')
        elif amount > self.maxWithdraw:
            # return f'bank fokir hoye jabe. you can not withdraw more than {self.maxWithdraw}'
            print(
                f'bank fokir hoye jabe. you can not withdraw more than {self.maxWithdraw}')
        else:
            self.balance -= amount
            # return f'here is your money {amount}'
            print(f'here is your money {amount}')
            print(f'your balance after withdraw {self.balance}')
            print(f'your balance after withdraw {self.getBalance()}')


brackBank = Bank(15000)
brackBank.withdraw(25)
brackBank.withdraw(500000000)
brackBank.withdraw(1000)

dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.getBalance())
