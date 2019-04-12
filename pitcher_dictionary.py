# # = 0,Name = 1,Team,W,L,SV,G,GS,IP,K/9,BB/9,HR/9,BABIP,LOB%,GB%,HR/FB,ERA,FIP,xFIP,WAR

import csv


pitcherDict = {} #where all data is stored
cats = [] #list of ll categories of data being stored
pitcherList = []

# adds pitchers names into dict
with open('DashboardStats') as file:
    reader = csv.reader(file)

    for row in reader:
        pitcherDict[(row[1])] = {}
        if row[1] != 'Name':
            pitcherList.append(row[1])

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
        for key in pitcherDict:
            if row[1] == key:
                count = 0
                for c in row:
                    pitcherDict[key][cats[count]] = c
                    count += 1

with open('AdvancedStats') as file:
    reader = csv.reader(file)
    for row in reader:
        for key in pitcherDict:
            if row[0] == key:
                count = 19
                for c in row:
                    if count == 19:
                        pop = "oh no"
                    else:
                        pitcherDict[key][cats[count]] = c
                        count += 1

with open('BattedBalls') as file:
    reader = csv.reader(file)
    for row in reader:
        for key in pitcherDict:
            if row[0] == key:
                count = 30
                for c in row:
                    if count == 30:
                        pop = "oh no"
                    else:
                        pitcherDict[key][cats[count]] = c
                        count += 1

