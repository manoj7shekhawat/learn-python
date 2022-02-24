#!/usr/bin/env python3

import os
import art
import random
import game_data

# For clearing console
clear = lambda: os.system('clear')

myScore = 0
isWinning = False


def increaseScore():
    global myScore
    myScore += 1


def displayLogo():
    print(art.logo)


def displayVs():
    print(art.vs)


def displayPlayer(type, player):
    print(f"Compare {type}: {player['name']}, {player['description']}, {player['country']}")


# Pick on random record
playerA = random.choice(game_data.data)


while True:
    clear()
    displayLogo()

    if isWinning:
        print(f"You're right! Current score: {myScore}.")

    displayPlayer("A", playerA)

    displayVs()

    playerB = random.choice(game_data.data)
    # If same player then choose other one
    while playerB['name'] == playerA['name']:
        playerB = random.choice(game_data.data)

    displayPlayer("B", playerB)

    ch = input("Who has more followers: 'A' or 'B': ")
    if ch == 'A' and playerA['follower_count'] > playerB['follower_count']:
        isWinning = True
        increaseScore()
    elif ch == 'B' and playerB['follower_count'] > playerA['follower_count']:
        isWinning = True
        increaseScore()
        playerA = playerB
    elif ch == 'A' and playerA['follower_count'] < playerB['follower_count']:
        clear()
        displayLogo()
        print(f"Sorry that is wrong, your final score: {myScore}")
        break
    elif ch == 'B' and playerA['follower_count'] > playerB['follower_count']:
        clear()
        displayLogo()
        print(f"Sorry that is wrong, your final score: {myScore}")
        break
