#!/usr/bin/env python3

num = int(input("Enter number to check: "))

def is_prime(num):
    result = True
    if num == 1:
        return False
    if num == 2:
        return True

    for x in range(2, int(num/2) + 1):
        #print(x)
        if num % x == 0 and num != x:
            result = False
            break

    return result


if is_prime(num):
    print("It's a prime number.")
else:
    print("It's not a prime number.")