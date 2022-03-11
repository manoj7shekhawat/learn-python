import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

myDict = { row.letter: row.code for (index, row) in df.iterrows() if row.letter != "letter" }

#print(myDict)

name = input("Enter your name: ")

print(f"{[ myDict[n.upper()] for n in name]}")