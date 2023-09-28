def multiple():
    return 3, 4


print(multiple())

things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam'
print(things)
print(type(things))
print(things[0])
print(things[-2])
print(things[3:6])


if 'phone' in things:
    print("Exists")

for item in things:
    print(item)

# things[0] = 'wagon'  # 'tuple' object does not support item assignment
# print(things)


print(len(things))
mega = ([2, 3, 4], [6, 8, 9, 5])
print(mega)
print(type(mega))
print(mega[0])
# because list is mutable
mega[0][1] = 666
print(mega[0])
