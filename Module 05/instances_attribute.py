class Shop:
    shoppingMall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # cart is an instance attribute

    def addToCart(self, item):
        self.cart.append(item)


mehzabeen = Shop('Meh Jabeen')
mehzabeen.addToCart("Shoes")
mehzabeen.addToCart('Phone')
print(mehzabeen.cart)

nisho = Shop('Noisho')
nisho.addToCart('cap')
nisho.addToCart('watch')
print(nisho.cart)

apurba = Shop('age purbo chilo')
apurba.addToCart('chiruni')
print(apurba.cart)
