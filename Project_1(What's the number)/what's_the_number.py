import random

# generating random number between 1 and 10
number = random.randint(1, 10)
user_guess = None

while user_guess != number:
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess == number:
        print("Congratulations You Won!")
        break
    else:
        print("Nope, sorry, Try Again.")
