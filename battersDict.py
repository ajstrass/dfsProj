# Creates dictionary of each teams batting order
import csv

# dictionary storing batting order
lineupDict = {}
listOfBatters = []
# parse through and put each team in the dict
with open('lineupData.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        lineupDict[row[0]] = {}

# Number of teams on slate
numTeams = 0
for x in lineupDict:
    numTeams += 1

# Sets default value in dictionary to "pitcher"
for x in lineupDict:
    for y in range(1, 10):
        lineupDict[x][y] = 'Pitcher'

# Begins filling in batters
with open('lineupData.csv') as file:
    reader = csv.reader(file)
    # uses skip to skip the first line of data
    skip = True
    for row in reader:
        if skip == True:
            skip = False
        # skips the starting pitcher
        elif row[5] == 'SP':
            "nada"
        else:
            # fills in the batters
            team = row[0]
            name = row[4]
            pos = int(row[5])
            lineupDict[team][pos] = name
            listOfBatters.append(name)

# pops cataegory names from dictionary
lineupDict.pop('team code')