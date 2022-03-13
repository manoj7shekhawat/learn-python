import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

myDict = { row.letter: row.code for (index, row) in df.iterrows() if row.letter != "letter" }

name = input("Enter your name: ")

isOn = True
while isOn:
    try:
        myList = [ myDict[n.upper()] for n in name]
        print(f"{myList}")
        isOn = False
    except KeyError:
        print("Sorry please enter correct input")
        name = input("Enter your name: ")
