import csv

# Dictionary for storing all 2019 league avg stats
las19Dict = {}

las18Dict = {}

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
                name = c + '_19'
                las19Dict[name] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                las19Dict[laCats[sCount] + '_19'] = v
                sCount += 1
        count += 1

# places 2019 dashboard stats into dictionary
with open('LA-DashboardStats-2018') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                name = c + '_18'
                las19Dict[c] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                las19Dict[laCats[sCount] + '_18'] = v
                sCount += 1
        count += 1

# places 2019 advanced stats into dictionary
with open('LA-AdvancedStats-2019') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                name = c + '_19'
                las19Dict[name] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                las19Dict[laCats[sCount] + '_19'] = v
                sCount += 1
        count += 1

# places 2019 batted ball stats into dictionary
with open('LA-BattedBalls-2019') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                name = c + '_19'
                las19Dict[name] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                las19Dict[laCats[sCount] + '_19'] = v
                sCount += 1
        count += 1

# places 2018 batted ball stats into dictionary
with open('LA-BattedBalls-2018') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                name = c + '_18'
                las19Dict[name] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                las19Dict[laCats[sCount] + '_18'] = v
                sCount += 1
        count += 1


print(las19Dict)
