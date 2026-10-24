"""Small terminal guessing game with input validation."""

import random


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0

    print("Welcome to Guess the Number!")

    while True:
        try:
            raw_guess = input("Enter your guess (between 1 and 100): ")
        except (EOFError, KeyboardInterrupt):
            print("\nGame ended.")
            return

        try:
            guess = int(raw_guess.strip())
        except ValueError:
            print("Please enter a whole number between 1 and 100.")
            continue

        if not 1 <= guess <= 100:
            print("Please enter a number between 1 and 100.")
            continue

        number_of_guesses += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {number_of_guesses} guesses!")
            return


if __name__ == "__main__":
    guess_the_number()
