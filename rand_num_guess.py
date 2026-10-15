#!/usr/bin/env python3\
# Created By:Kamche
# Created on: September 24, 2026
# This program will guess a random number and
# and see if it match with the user guess.
import random


def main():
    # Ask the user to pick a number between 0 and 9
    random_number = random.randint(0, 9)
    user_guess = int(input("Guess a number between 0 and 9: "))

    # Get the random number and convert to an integer
    if user_guess == random_number:
        print("You guessed correctly! Good Job!")
    else:
        print("You guessed wrong.")
        print("The correct answer was: {}".format(random_number))


if __name__ == "__main__":
    main()
