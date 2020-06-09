import random
random_number = random.randint(1,10)

i = 0
number_found = False

while i < 3:
    users_guess = int(input("Guess: "))
    # increment for each guess, not for each wrong guess
    i = i + 1
    if users_guess == random_number:
        print("You won")
        number_found = True
        # no need to include number_found in while condition to exit the loop, just break is enough
        break

if number_found == False:
    print("Sorry you failed")