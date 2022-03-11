import pandas as pd

myDict = {
    "student" : ["Manoj", "Yuvraj", "Mittal"],
    "score": [91, 99, 93]
}

print("Iterating Dictionary")
for (k, v) in myDict.items():
    print(f"Key: {k} Value: {v}")

myDf = pd.DataFrame(myDict)

print("Iterating DF Dictionary way")
# iterating DF Dictionary way
for (k, v) in myDf.items():
    print(f"Key: {k} \nValue: {v}")

print("Proper way of iterating DF")
# Proper way of iterating DF
for (index, row) in myDf.iterrows():
    print(f"Index: {index} Student: {row.student} Score: {row.score}")


