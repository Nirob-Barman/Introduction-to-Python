balance = 3000  # global scope variable


def buyThings(item, price):
    # global variable can be accessed without using the global keyword
    # but to modify use global keyword

    dreamPhone = 'xPhone'
    # balance = 600  # local scope variable
    global balance  # global vaiable accessing
    print(f'Previous Balance:', balance)
    balance = balance - price
    print(f'Balance inside the function after buying {item}:', balance)


buyThings('sunglass', 1000)
# print(dreamPhone) #error
