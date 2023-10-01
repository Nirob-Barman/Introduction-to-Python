class Shop:
    cart = []  # cart is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def addToCart(self, item):
        self.cart.append(item)


mehzabeen = Shop('Meh Jabeen')
mehzabeen.addToCart("Shoes")
mehzabeen.addToCart('phone')
print(mehzabeen.cart)

nisho = Shop('Noisho')
nisho.addToCart('cap')
nisho.addToCart('watch')
print(nisho.cart)
