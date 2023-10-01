class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def sendSMS(self, phone, sms):
        text = f'sending to : {phone} {sms}'
        print(text)


myPhone = Phone('Kala Chan', "Oppo", 9800)
print(myPhone.owner, myPhone.brand, myPhone.price)

herPhone = Phone('She Amar Jaan', "iphone", 120000)
print(herPhone.owner, herPhone.brand, herPhone.price)
