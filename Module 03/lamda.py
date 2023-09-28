# lambda

# def doubled(x):
#     return x*2

# doubled = lambda num : num * 2
# squared = lambda num : num * num

# result = doubled(44)
# output = squared(9)

# print(result)
# print(output)

def doubled(num): return num * 2
def squared(num): return num * num


result = doubled(44)
output = squared(9)

print(result)
print(output)


def add(x, y): return x+y


sum = add(11, 33)
print(sum)

numbers = [12, 56, 78, 56, 78, 56, 12, 6, 98]
doubledNumbers = map(doubled, numbers)
# print(doubledNumbers)
print(numbers)
print(list(doubledNumbers))

doubledNums = map(lambda x: x*2, numbers)
# print(doubledNums)
print(list(doubledNums))


actors = [
    {'name': 'sabana', 'age': 65},
    {'name': 'sabnoor', 'age': 45},
    {'name': 'sabila noor', 'age': 30},
    {'name': 'srabonti', 'age': 38},
    {'name': 'saon', 'age': 47},
]

juniors = filter(lambda actor: actor['age'] < 40, actors)
print(list(juniors))
Fivers = filter(lambda actor: actor['age'] % 5 == 0, actors)
print(list(Fivers))
