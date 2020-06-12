coordinates = (1, 2, 3)
# approach 1
print(coordinates[0] * coordinates[1] * coordinates[2])
# let's say we want to use these values in quite a few places in our program, our code is getting too long
# approach 2
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# approach 3: unpacking (less code)
x, y, z = coordinates
# line 10 is same as line 6-8
# When Python interpreter sees this statement, it will get the 1st item in this tuple and assign it to the x variable. so on
# so we are unpacking this tuple into 3 variables
print(x)
print(y)
print(z)

# we can use this feature for lists as well: we can unpack our list into 3 variables
values = [4, 5, 6]
a, b, c = values
print(a)
print(b)
print(c)