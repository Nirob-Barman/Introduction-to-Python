class Shooping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def addToCart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkOut(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price:', total)
        if amount < total:
            print(f'please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')

    def removeItems(self, item):
        pass


swapan = Shooping('Alan Swapan')
swapan.addToCart('alu', 50, 6)
swapan.addToCart('dim', 12, 24)
swapan.addToCart('rice', 50, 5)

print(swapan.cart)
# swapan.checkOut(600)
swapan.checkOut(1600)
