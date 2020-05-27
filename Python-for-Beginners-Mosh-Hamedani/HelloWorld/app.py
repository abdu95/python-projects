course = 'Python for Beginners'
# [0] --> 'P'
print(course[0])
# negative index: get char starting from the end
# second char from the end: 'r'
print(course[-2])
# Python interpreter will return all the characters
# starting with this index [0] all the way to this second index [3]
# but it does not return the character at this [3] index ('h').
# --> Pyt
print(course[0:3])
# default values for start and end index
# return all the characters till the end of the string --> 'Python for Beginners'
print(course[0:])
# exclude first character and return all the characters till the end of the string
print(course[1:])
# --> Pytho
print(course[:5])
# 0 will be assumed as start index, length of the string will be assumed as the end index
print(course[:])
# copy of course variable
another = course[:]
print('another ' + another)


