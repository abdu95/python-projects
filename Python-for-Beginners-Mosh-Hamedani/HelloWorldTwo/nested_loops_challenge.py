# Using your for loop you need to iterate over this list.
# In each iteration you get one number, this determines the number of x's
# to be displayed on that particular line. So if you want to cheat,
# you can get this number and multiply by a string that contains x,
# so if you multiply x by 5, we'll get 5 x's, that's not what I want you to do.
numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     print('x' * number)

for number in numbers:
    element = ""
    for item in range(number):
        element += "x"
    print(element)