# we use while loops to execute a block of code multiple times.
# we use for loop to iterate over items of a collection, such as a string.
# Because a string is a sequence of characters, so it looks like a collection
# so we can use a for loop to iterate over each character in a string

i = 1
# in 1st iteration, item = P, in 2nd iteration item = y
# in while loop, loop is terminated when while condition is not satisfied OR break operation is called
# in for loop, loop is finished when there is no item left in the collection
for item in 'Python':
    print(f"#:{i}  {item}")
    i = i+1

# list: [] --> list of items (numbers, names)
for item in ['Mosh', 'Abdu', 'Sarah']:
    print(f"Student #{i} {item}")

for item in [1, 2, 3, 4]:
    print(item)

print("loop with big numbers")
for item in range(10):
    print(item)
# range function creates an object, that we can iterate over
# in each iteration, this object will spit out a new number.

print("start")
for item in range(5, 10):
    print(item)

print("add step: 2 steps forward")
for item in range(5, 10, 2):
    print(item)