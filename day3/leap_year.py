#!/usr/bin/env python3

# ๐จ Don't change the code below ๐
year = int(input("Which year do you want to check? "))
# ๐จ Don't change the code above ๐

#Write your code below this line ๐

"""
every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 รท 4 = 500 (Leap)

2000 รท 100 = 20 (Not Leap)

2000 รท 400 = 5 (Leap!)

So the year 2000 is a leap year.
"""

if ( year % 4 == 0):
    if ( year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")