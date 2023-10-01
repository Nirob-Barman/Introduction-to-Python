from typing import Any


def call():
    print('Calling someone i don\'t know')
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print("Calling one person")

    def sendSMS(self, phone, sms):
        text = f'sending sms to {phone} and message: {sms}'
        return text


myPhone = Phone()
print(myPhone.features)
print(myPhone.color)
print(myPhone.brand)
print(myPhone.price)
myPhone.call()
result = myPhone.sendSMS(41524, 'I forgot to miss you')
print(result)
