numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [n*n for n in numbers]

#Write your code 👆 above:

print(squared_numbers)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:

print(result)


# Files excercise
num1 = []
num2 = []
with open("file1.txt", mode="r") as f1:
    num1 = f1.readlines()

with open("file2.txt", mode="r") as f2:
    num2 = f2.readlines()

num1 = [int(n.strip()) for n in num1]
num2 = [int(n.strip()) for n in num2]

result = [n for n in num1 if n in num2]

print(result)


# Ex 4

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = sentence.split(" ")
print(f"{words}")

result = { n : len(n) for n in words}


print(result)


# Ex 5

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# (0°C × 9/5) + 32 = 32°F
weather_f = { k: (v * 9/5) + 32 for (k, v) in weather_c.items()}

print(weather_f)