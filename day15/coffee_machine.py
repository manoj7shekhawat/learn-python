#!/usr/bin/env python3
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def haveMoney(coffee):
    if getCoffeePrice(coffee) < moneyPaid():
        return True
    else:
        return False

def haveResources(coffee):
    if coffee == "espresso":
        if resources["water"] >= MENU[coffee]["ingredients"]["water"] and \
                resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
            return True
        else:
            return False
    else:
        if resources["water"] >= MENU[coffee]["ingredients"]["water"] and \
            resources["milk"] >= MENU[coffee]["ingredients"]["milk"] and \
            resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
            return True
        else:
            return False


def adjustResources(water, coffee, milk):
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["milk"] -= milk

def makeCoffee(cof):
    water = MENU[cof]["ingredients"]["water"]
    coffee = MENU[cof]["ingredients"]["coffee"]
    # TODO: milk
    if cof == "espresso":
        adjustResources(water, coffee, 0)
    else:
        milk = MENU[cof]["ingredients"]["milk"]
        adjustResources(water, coffee, milk)
    addMoney(cof)

money = 0.0

# quarters = 0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
quarters = 0
dimes = 0
nickles = 0
pennies = 0

def takeMoney():
    global quarters, dimes, nickles, pennies
    print("Please insert coins")
    quarters = int(input("Quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))


def addMoney(coffee):
    global money
    money += getCoffeePrice(coffee)

def moneyPaid():
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

def getCoffeePrice(coffee):
    return MENU[coffee]["cost"]

def change(coffee):
    return round(moneyPaid() - getCoffeePrice(coffee), 2)

# Print report
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# Step 1

while True:

    ch = input("What would you like (espresso/latte/cappuccino): ")

    if ch == "stop":
        print("Stopping machine")
        sys.exit(0)
    elif ch == "report":
        report()
    else:
        if haveResources(ch) == False:
            print("Sorry don't have resources")
        elif takeMoney() or haveMoney(ch) == False:
            print("Sorry you don't have enough money")
        else:
            makeCoffee(ch)
            print("Here is: $" + str(change(ch)) + " in change")
            print(f"Here is your {ch}, Enjoy")
