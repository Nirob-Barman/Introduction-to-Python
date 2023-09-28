name1 = 'sakib\'s khan'  # escape
name2 = "sakib khan"
name3 = """
Sakib khan
sakib khan
Tamim khan
"""
print(name1)
print(name2)
print(name3)


# mutable means chagneable
for char in name2:
    print(char)
print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])
# immutable means you can't change it

# name2[2] = 'R'  # 'str' object does not support item assignment
# print(name2)

if 'khan' in name2:
    print('exists')
print(name2.upper())
