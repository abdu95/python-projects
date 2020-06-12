# Tuples are similar to lists so we can use them to store a list of items.
# But unlike lists we can not modify them, we cannot add new items, we cannot remove existing items - tuples are immutable.
# we use parenthesis to define tuples
numbers = (1, 2, 3, 3)
# .count - to count the number of occurrences in an item
print(numbers.count(3))
#  index - to find the index of the first occurrence of an item
print(numbers.index(2))
# we can only get information about a tuple, we can't change it.
# other methods that start with two underscores, we refer to these as magic methods __add__ __class__
# get access individual items using squre bracketts
print(numbers[1])
numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

