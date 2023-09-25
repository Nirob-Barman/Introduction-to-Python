# default arguments
def sum(a, b, c=0, d=0, e=0):
    result = a+b+c+d+e
    return result


total = sum(4, 8)
print(total)
total = sum(4, 8, 5)
print(total)


# args
# def allSum(*numbers):
def allSum(num1, num2, *numbers):
# def allSum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        # print(num)
        sum += num
    return sum


total = allSum(4, 5, 6, 7, 8)
# total = allSum(4, 5)
# total = allSum(4)  # error
print("All sum:", total)


def doALot(*args):
    print(args)
