#!/usr/bin/env python3

import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_ques = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

myCards = []
comCards = []
myTotal = 0
comTotal = 0


def getMyCards():
    global myTotal
    newCard = random.choice(cards)
    if newCard == 11 and myTotal + newCard > 21:
        print("Switched 11 to 1")
        newCard = 1
    myCards.append(newCard)
    myTotal = sum(myCards)
    return myTotal


def getComCards():
    global comTotal
    newCard = random.choice(cards)
    if newCard == 11 and myTotal + comTotal > 21:
        print("Switched 11 to 1")
        newCard = 1
    comCards.append(newCard)
    comTotal = sum(comCards)
    return comTotal


getMyCards()
getMyCards()
getComCards()

moreCards = "y"


def printCurrent(result):
    print(f"Your cards {myCards}, current score: {myTotal}")
    print(f"Computer's cards: {comCards}, current score:  {comTotal}")
    print(result)


while play_ques == "y":
    if moreCards == "y":
        print(f"Your cards {myCards}, current score: {myTotal}")
        print(f"Computer's first card: {comCards[0]}")
        moreCards = input("Type 'y' to get another card, type 'n' to pass: ")
    if moreCards == "y":
        getMyCards()
        if myTotal > 21:
            printCurrent("You Lost!!")
            break
    elif random.randint(0, 1) == 0 or comTotal < 17:
        getComCards()
        if random.randint(0, 1) == 0:
            moreCards = "y"
        if comTotal > 21:
            printCurrent("You Win!!")
            break
    else:
        if myTotal == comTotal:
            printCurrent("DRAW")
        elif myTotal > comTotal:
            printCurrent("You Win!!")
        elif myTotal < comTotal:
            printCurrent("You Lost!!")
        break
