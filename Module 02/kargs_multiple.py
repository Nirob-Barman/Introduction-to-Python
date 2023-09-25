def fullName(first, last):
    # name = f'{first} {last}'
    name = f'Full name is: {first} {last}'
    return name


# take parameters in order(serial wise)
name = fullName('Abul', 'Hasan')
print(name)
name = fullName(last='Abul', first='Hasan')
print(name)
name = fullName(last='Hasan', first='Abul')
print(name)


# def famous(**kargs) # key arguments

def famousName(first, last, **addition):
    name = f'{first}  {last}'
    print(addition)
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name


name = famousName(first='Abul', last='Ali', title='Hasan', Middle='Thief')
print(name)


# def functionName(num1,num2,*args,**kargs):

# return multiple things from an array
def aLot(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    # return sum, sub, mul  # tupple
    return [sum, sub, mul]  # list


everyThing = aLot(2, 4)
print(everyThing)
