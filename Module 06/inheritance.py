# base class, parent class,  common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'learning python and practicing'


class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dualSIM) -> None:
        self.dualSIM = dualSIM
        super().__init__(brand, price, color, origin)

    def phoneCall(self, number, text):
        return f'sending SMS to: {number}'

    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dualSIM}'


class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def changeLens(self):
        pass

# inheritance


myPhone = Phone('iphone', 120000, 'silver', 'china', True)
print(myPhone)
print(myPhone.brand)
print(myPhone.color)
