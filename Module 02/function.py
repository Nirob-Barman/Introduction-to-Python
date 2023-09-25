# define


def doubleIt(num):
    result = num*2
    print(result)
    return result


doubleIt(8)
doubleIt(5)


def sum(a, b):
    result = a+b
    return result


total = sum(3, 5)
print('Total value:', total)

final = doubleIt(total)
print('Final value: ', final)
