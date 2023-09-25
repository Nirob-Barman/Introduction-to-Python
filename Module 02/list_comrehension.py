numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = []
for num in numbers:
    if num % 2 == 1:
        odds.append(num)
print(odds)

odds = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)

oddNums = [num for num in numbers]
print(oddNums)

oddNums = [num for num in numbers if num % 2]
print(oddNums)
oddNums = [num for num in numbers if num % 2 and num % 5 == 0]
print(oddNums)

ageComb = []
players = ['sakib', 'musfik', 'mustafiz']
ages = [38, 38, 32]
for player in players:
    print('player:', player)
    for age in ages:
        print(player, age)
        ageComb.append([player, age])
print(ageComb)

ageCombination = [[player, age] for player in players for age in ages]
print(ageCombination)
ageCombination = [(player, age) for player in players for age in ages]
print(ageCombination)
