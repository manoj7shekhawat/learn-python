#!/usr/bin/env python3
import sys

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


cm = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()


while True:
    ch = input("Welcome to coffee maker. Choose (latte, espresso, cappuccino, report, stop): ")

    if ch == "stop":
        print("Stopping machine!!")
        sys.exit(0)
    elif ch == "report":
        cm.report()
    elif cm.is_resource_sufficient(menu.find_drink(ch)) and mm.make_payment(menu.find_drink(ch).cost):
        cm.make_coffee(menu.find_drink(ch))
