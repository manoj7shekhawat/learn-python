#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

"""
Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."
"""

true = 0
love = 0

for x in (name1 + name2).upper():
    if x == "T" or x == "R" or x == "U" or x == "E": true += 1

for x in (name1 + name2).upper():
    if x == "L" or x == "O" or x == "V" or x == "E": love += 1

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 50 > score > 40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


