numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8]
numbers2 = []
for number in numbers:
    if number not in numbers2:
        # writing numbers.append(number) giving MemoryError
        numbers2.append(number)

print(numbers2)

# disclaimer: just figured out that it is not possible to add item to array with square bracket
items = [1, 2, 3]
# in JavaScript, it is possible to add item in index 3
# but Python assumes you are assigning an item in index 3
# there is no item in index 3, therefore: IndexError: list index out of range
# items[3]