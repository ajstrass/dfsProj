import csv
pitcherDict = {} #where all data is stored
cats = [] #list of ll categories of data being stored
pitcherList = []
# adds pitchers names into dict
with open('DashboardStats') as file:
    reader = csv.reader(file)
    for row in reader:
        pitcherDict[(row[0])] = {}
        if row[0] != 'Name':
            pitcherList.append(row[0])

# adds categories to list
with open('DashboardStats') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count < 1:
            for x in row:
                cats.append(x)
        count += 1
with open('AdvancedStats') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count < 1:
            for x in row:
                if x != 'Name':
                    cats.append(x)
        count += 1
with open('BattedBalls') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count < 1:
            for x in row:
                if x != 'Name':
                    cats.append(x)
        count += 1
#print(pitcherDict)
pitcherDict.pop('Name')
# creats the dictionary values for all categories
# initialized to 0
for key in pitcherDict:
    for cat in cats:
        pitcherDict[key][cat] = 0
# updates correct values of categories
with open('DashboardStats') as file:
    reader = csv.reader(file)
    for row in reader:
        for pitcher in pitcherDict:
            if row[0] == pitcher:
                for x in range(0, 19):
                    pitcherDict[pitcher][cats[x]] = row[x]
with open('AdvancedStats') as file:
    reader = csv.reader(file)
    for row in reader:
        for pitcher in pitcherDict:
            if row[0] == pitcher:
                for x in range(0, 11):
                    pitcherDict[pitcher][cats[x + 19]] = row[x + 1]

with open('BattedBalls') as file:
    reader = csv.reader(file)
    for row in reader:
        for pitcher in pitcherDict:
            if row[0] == pitcher:
                for x in range(0, 18):
                    pitcherDict[pitcher][cats[x + 30]] = row[x + 1]

# Removes % sign from any rate values
for pitcher in pitcherDict:
    for category in pitcherDict[pitcher]:
        try:
            if '%' in pitcherDict[pitcher][category]:
                pitcherDict[pitcher][category] = pitcherDict[pitcher][category].rstrip(' %')
        except:
            "nothing"

