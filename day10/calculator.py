#!/usr/bin/env  python3

import sys
import art

print(art.logo)

num_1 = 0.0
num_2 = 0.0
op = ""

def calculation(op, n1, n2):
    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "*":
        result = n1 * n2
    elif op == "/":
        result = n1 / n2
    print(f"{n1} {op} {n2} = {result}")
    return result


def take_input(num):
    global num_1
    global num_2
    global op
    if num == 0.0:
        num_1 = float(input("Enter first number: "))
    else:
        num_1 = num
    print("+\n-\n*\n/")
    op = input("Pick the operation: ")
    num_2 = float(input("Enter second number: "))


def next_choice(res):
    ch = input(f"Type 'y' to continue with {result}, or 'n' to start new calculation, or 'stop' to terminate: ")
    if ch == "y":
        take_input(result)
    elif ch == "n":
        take_input(0.0)
    else:
        print("Stopping Calculator!!")
        sys.exit(0)

take_input(0.0)

while True:
    result = calculation(op, num_1, num_2)
    next_choice(result)
