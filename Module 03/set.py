# list --> []
# tupe --> ()
# set --> {}
# set: unique items collection. No duplicate
numbers = [12, 56, 78, 56, 78, 56, 12, 6, 98]
print(numbers)
numbersSet = set(numbers)
print(numbersSet)
numbersSet.add(55)
print(numbersSet)

# print(numbersSet[2])  # set' object is not subscriptable
# numbersSet[1] = 9  # 'set' object does not support item assignment

numbersSet.remove(6)
print(numbersSet)

for item in numbersSet:
    print(item)

if 9 in numbersSet:
    print("9 Exists")
elif 98 in numbersSet:
    print("98 Exists")

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B)  # A intersection B
print(A | B)  # A union B
