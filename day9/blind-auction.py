#!/usr/bin/env python3

import art
import os

clear = lambda: os.system('clear')

print(art.logo)

print("Welcome to blind auction!!")

ch = "yes"

all_bids = {}

while ch == "yes":
    name = input("What is your name: ")
    bid = int(input("Your bid : $"))
    all_bids[name] = bid
    ch = input("More bidding 'yes' or 'no': ")
    clear()

max_bid = 0
winner = ""

for x in all_bids:
    bid = all_bids[x]

    if bid > max_bid:
        max_bid = bid
        winner = x

print(f"Winner is {winner} with bid ${max_bid}")
