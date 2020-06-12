# string recap in line 25

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# list is shown (with square brackets)
print(names)

print(f"first item: {names[0]}")
print(f"last item: {names[-1]}")

# colon to select a range of items
# starting from the index of 2, that is Mosh, all the way to the end of the string
print(names[2:])
# specify end index
# return all the items up to index 4, but it doesn't include the item at index 4
print(names[2:4])
# just like strings, these square brackets don't modify our original list,
# they simply return a new list
# show new list with three items:
print(names[2:])

# update (modify) first item in the list
names[0] = "Jon"
print(names)

# <string recap>
name = "John"
print(f"first char of string: {name[0]}")
#  negative index
print(f"last char of string: {name[-1]}")
# starting from index 1, until (not including) index 3
print(name[1:3])
# starting from index 1, all the way to the end
print(name[1:])
# starting from index 0, until (not including) index 2
print(name[:2])
print(f"default: {name[:]}")
# starting from index 0, until (not including) last item
print(name[:-1])
#  from the beginning to the end of the list
print(name[:])