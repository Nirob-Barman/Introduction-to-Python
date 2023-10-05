# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method

class Shopping:
    cart = []  # class attribute #static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = name  # instance attribute
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply(a, b):
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self, item):
        # print(self.name)
        print('hudai dekhi kintu kinmu just ac er hawa khaite aschi', item)


# Shopping.purchase('a', 2, 3, 4)
# Shopping.purchase(2, 3, 3)
basundara = Shopping('basu en dhara', 'not popular location')
basundara.purchase('lungi', 500, 1000)
# basundara.hudai_dekhi('lungi')
Shopping.hudai_dekhi('Lungi')

# static method
Shopping.multiply(4, 6)

basundara.multiply(6, 9)
