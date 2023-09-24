# in, not, not in, is, is not
# > ,< ,>= ,<= ,== ,!==

# a = 7
# a = 4
a = 2

if a > 5:
    print('greater than 5')
    print('How much more:', a-5)
elif a > 3:
    print("greater than 3 less than 5")
elif a == 2:
    print("Equal to value: 2")
else:
    print("Less than 5")

boss = False
if boss is True:
    print("Boss is True")
else:
    print("Boss is False")

if boss is not True:
    print("Boss is False")
else:
    print("Boss is True")

# nested conditions

boss = True
coin = 'head'
if boss == True:
    print("True")
    if coin == 'tail':
        print("Tail")
    else:
        print("Head")
else:
    print('False')
