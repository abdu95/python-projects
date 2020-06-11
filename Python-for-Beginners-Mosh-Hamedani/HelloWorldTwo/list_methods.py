numbers = [5, 2, 1, 7, 4]
# add at the end
numbers.append(20)
# add in the middle, or at the beginning
# two params:
# 1: index at which we want to insert this new item.
# 2: object we want to add to this list
numbers.insert(0, 10)
# pass the item that you want to remove
numbers.remove(5)
# remove all the items in the list
# numbers.clear()
# remove the last item in a list
numbers.pop()
# to check for the existence of an item in our list, you can call the index() method
# index returns the index of the first occurrence of this item
# if we pass a number that doesn't exist in this list: ValueError. 50 is not in the list
# print(numbers.index(50))
# another way to check for the existence of an item we can use the 'in' operator
print(50 in numbers)  # False
# method for counting the occurrences of an item (we have only one 2 in the list)
print(numbers.count(2))
# sort the list
print(numbers.sort())
# return value: None - is an object in python that represents the absence of a value.
# sort method doesn't really return any values it simply sorts this list, in place,
# print the list to see how its sorted (ascending order)
print(numbers)
# sort the items in descending order
numbers.reverse()
print(numbers)
# get a copy of our list
#  if you make any changes to our original list, (add new items, remove), these operations are not going to impact our second list.
numbers2 = numbers.copy()
print(numbers)
numbers[4] = 100
print(numbers)  # numbers changed
print(numbers2)  # numbers2 not changed


# check for the existence of a character or a sequence of a character in a string,
name = "Abdu"
print("b" in name)  # True