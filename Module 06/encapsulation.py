# encapsulation --> hide details
# access modifier: public, protected, private

class Bank:
    def __init__(self, holderName, initialDeposit) -> None:
        self.holderName = holderName  # public attribute
        self._branch = 'banani 11'  # protected
        self.__balance = initialDeposit  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Forkia taka nai'


rafsun = Bank('Choooto bro', 10000)

print(rafsun.holderName)
# print(rafsun.__balance)
rafsun.deposit(40000)
print(rafsun.get_balance())

rafsun.holderName = 'boro vai'
print(rafsun.holderName)
print(rafsun._branch)
# print(dir(rafsun))
print(rafsun._Bank__balance)
