numbers = [12, 56, 78, 56, 78, 56, 12, 6, 98]

person1 = ['kala Chan', 'kalipur', 23, 'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key: value, key: value, key: value}

person = {'name': 'kala pakhi', 'address': 'kalipur',
          'age': 23, 'job': 'student'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
# mutable
person['language'] = 'python'
person['name'] = 'sada pakhi'
print(person)


for item in person:
    print(item)  # only key values

# special dictionary looping
for key, value in person.items():
    print(key, value)
