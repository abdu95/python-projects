# ask a DoB, calculate age, print on the terminal
birth_year = input('Birth year: ')
# Type error: we're subtracting a string (input) from an integer (2020)
# age = str(2020) + birth_year --> possible
# age = str(2020) - birth_year --> not possible
age = 2020 - int(birth_year)
print (age)

# int() -- str to int
# float() -- str to float
# bool() -- str to boolean
