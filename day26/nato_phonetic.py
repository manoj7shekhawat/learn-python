
myList = []

with open("nato_phonetic_alphabet.csv", mode="r") as fh:
    myList = fh.readlines()


myDict = {item.split(",")[0]: item.split(",")[1].strip() for item in myList if not item.startswith("letter")}

#print(myDict)

name = input("Enter your name: ")

nato_name = []

nato_name = [ myDict[n.upper()] for n in name]

print(f"Your NATO name:\n {nato_name}")