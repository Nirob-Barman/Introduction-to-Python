class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'

    def coding(self):
        return f'learning python and practicing'


class Phone:
    def __init__(self, brand, price, color, dualSIM) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dualSIM = dualSIM

    def run(self):
        return f'phone tipa tipi kore'

    def phoneCall(self, number, text):
        return f'sending SMS to: {number}'


class Camera:
    def __init__(self, brand, price, color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass

    def changeLens(self):
        pass

