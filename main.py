import random

number_to_guess = random.randint(1, 100)

print("Welcome to 'Guess the Number'!")
print("I picked a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Your guess: "))

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break
