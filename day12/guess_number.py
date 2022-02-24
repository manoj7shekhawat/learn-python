#!/usr/bin/env python3

import random
import art

print(art.logo)

print("Welcome to Number guessing game!!!")
print("Guess a number 1-100")

level = input("Which level you want to play 'easy' or 'hard': ")

# Get a random number
NUM = random.randint(0, 100)

noOfTries = 0
# Perl if (boolean) ? Y : N
noOfTries = 10 if level == "easy" else 5

print(f"You have {noOfTries} attempts to guess the number.")

found = False

for x in range(1, noOfTries):
    guess = int(input("Make a guess: "))
    if guess > NUM:
        print("Too high")
    elif guess < NUM:
        print("Too low")
    elif guess == NUM:
        print("You guessed it. You win")
        found = True
        break
    left = noOfTries - x
    print(f"You have {left} attempts left")

if found == False:
    print(f"Sorry you ran out of attempts. You Lost!! Number was {NUM}")