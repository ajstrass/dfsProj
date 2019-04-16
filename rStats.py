import csv
from pitcher_dictionary import *

# Dictionary for storing all 2019 league avg stats
lasDict19 = {}
lasDict18 = {}


for x in cats:
    lasDict19[x] = 0
    lasDict18[x] = 0

# list of all catagories being stored
laCats = []
sCount = 0
# places 2019 dashboard stats into dictionary
with open('LA-DashboardStats-2019') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                lasDict19[c] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                lasDict19[laCats[sCount]] = float(v)
                sCount += 1
        count += 1

# places 2018 dashboard stats into dictionary
with open('LA-DashboardStats-2018') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                lasDict18[c] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                lasDict18[laCats[sCount]] = float(v)
                sCount += 1
        count += 1

# places 2019 advanced stats into dictionary
with open('LA-AdvancedStats-2019') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                lasDict19[c] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                lasDict19[laCats[sCount]] = float(v)
                sCount += 1
        count += 1

# places 2019 batted ball stats into dictionary
with open('LA-BattedBalls-2019') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                lasDict19[c] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                lasDict19[laCats[sCount]] = float(v)
                sCount += 1
        count += 1

# places 2018 batted ball stats into dictionary
with open('LA-BattedBalls-2018') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                lasDict18[c] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                lasDict18[laCats[sCount]] = float(v)
                sCount += 1
        count += 1


#print(lasDict19['ERA'])
