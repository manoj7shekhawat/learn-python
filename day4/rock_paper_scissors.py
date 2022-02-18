#!/usr/bin/env python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if ch > 2 or ch < 0:
    print("Invalid choice, YOU Loose!!")
else:
    myList = [rock, paper, scissors]

    print(myList[ch])

    print("Computer Chose:")

    comCh = random.randint(0, 2)

    print(myList[comCh])

    if ch == comCh:
        print("It's a draw")
    elif ch == 0:
        if comCh == 2:
            print("You win!!")
        else:
            print("You Lose!!")
    elif ch == 1:
        if comCh == 0:
            print("You win!!")
        else:
            print("You Lose!!")
    else:
        if comCh == 1:
            print("You win!!")
        else:
            print("You Lose!!")
