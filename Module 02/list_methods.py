numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.insert(2, 9)
print(numbers)
numbers.insert(2, 91)
print(numbers)
if 91 in numbers:
    numbers.remove(91)
if 9 in numbers:
    numbers.remove(9)
print(numbers)
last = numbers.pop()
print(last)
print(numbers)

index = numbers.index(3)
print(index)

if 9 in numbers:
    index = numbers.index(9)
    print(index)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
