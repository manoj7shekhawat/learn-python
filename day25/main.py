
# TODO: Direct reading for file
# data = []
#
# with open("weather_data.csv", mode="r") as fileHandle:
#     data = fileHandle.readlines()
#
# for x in data:
#     print(x)

# TODO: Using csv module
# import csv
#
# temperatures = []
#
# with open("weather_data.csv", mode="r") as fileHandle:
#     data = csv.reader(fileHandle)
#
#     for x in data:
#         if x[1] != 'temp':
#             temperatures.append(int(x[1]))
#
#
# print(temperatures)


# TODO: Using pandas library
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# temperatures = data["temp"].to_list()
#
# total = 0
#
# for x in temperatures:
#     total += x
#
# print(f"Avg Temp: {round(total/len(temperatures), 2)}")
#
# print(f"Max Temp: {data['temp'].max()}")
#
# print(f"Row with max temp:\n {data[data['temp'] == data['temp'].max()]}")
#
# monTempInC = data[data.day == 'Monday'].temp
# monTempInF = (monTempInC * 9/5) + 32
# print(f"{float(monTempInC)} C --> {float(monTempInF)} F")


# TODO: Squirrel data analysis
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

# data["Primary Fur Color"]
uniqueSqsColors = data["Primary Fur Color"].unique()
myDict = {}

for x in uniqueSqsColors:
    if not isinstance(x, float):
        myDict[x] = 0

sId = []

for index, row in data.iterrows():
    if row['Unique Squirrel ID'] not in sId and not isinstance(row['Primary Fur Color'], float):
        sId.append(row['Unique Squirrel ID'])
        myDict[row['Primary Fur Color']] += 1

print(myDict)

myNewDict = {
    'Fur Color': myDict.keys(),
    'Count': myDict.values()
}

pd.DataFrame(myNewDict).to_csv("my_results.csv")
