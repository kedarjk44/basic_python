from random import randint

# Generates a number from 1 through 10 inclusive
#random_number = randint(1, 10)

guesses_left = 3
# Start your game!
random_number = randint(1, 10)
# print(random_number)
while guesses_left != 0:
    guess = int(input("Guess any number") )
    if guess == random_number:
        print("Congrats you guessed it right")
        break
    guesses_left -= 1
else:
    print("You lose, %d guesses left" % guesses_left)
