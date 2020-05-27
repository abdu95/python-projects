course = 'Python for Beginners'
# function shows no of chars
print(len(course))
# len also can be used to count the number of items in a list
# functions that are specific to strings: upper() lower() replace()
# when a function belongs to something else, or is specific to some kind of object, we refer to that function as a method
# len() print() are general purpose functions, they don't belong to strings or numbers or other kinds of objects.
print(course.upper())
# upper() method  does not change or modify our original string,
# in fact it creates a new string and returns it
print(course)
print(course.lower())
# find() - to find a character or a sequence of characters in a string (case-sensitive)
# return the index of the first occurrence of that character --> 0
print(course.find('P'))
# -1 --> because there is no big O in the string
print(course.find('O'))
# We can also pass a sequence of characters
print(course.find('Beginners'))
print(course.replace('P', 'J'))
print(course.replace('Beginners', 'Absolute Beginners'))
# check if this string contains the word python
# this is an expression that produces a boolean value
# True
print('Python' in course)
# False
print('python' in course)

print(course.title())


