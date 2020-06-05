temperature = 40

# expression - code that produces a (boolean) value
if temperature == 40:
    print("It's a super hot day")
elif temperature < 30:
    print("It's not a hot day")
elif temperature >= 30:
    print("It's a hot day")
else:
    print("It's usual day")