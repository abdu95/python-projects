import random
random_number = random.randint(1,10)

# if user guess is equal to random_number, say you win
# check which attempt
#    if attempt < 3
#   user guess is not equal to random_number, increment i, ask input again
i = 0
number_found = False

while i < 3 or number_found == False:
    users_guess = int(input("Guess: "))
    if users_guess == random_number:
        print("You win")
        number_found = True
    else:
        i = i + 1

if number_found == False:
    print("Sorry you failed")

# 3 chances to make a guess