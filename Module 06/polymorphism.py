# poly --> many (multiple)
# morph --> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def makeSound(self):
        print('animal making some sound')


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print('meow meow')


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print('gheu gheu')


class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print('beh beh beh')


don = Cat('Real Don')
don.makeSound()

shepard = Dog('Local Shephard')
shepard.makeSound()

mess = Goat('L M')
mess.makeSound()

less = Goat('gora gori')

animals = [don, shepard, mess, less]
for animal in animals:
    animal.makeSound()
