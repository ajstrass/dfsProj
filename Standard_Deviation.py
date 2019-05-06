import csv
from pitcher_dictionary import *
standardDeviationDict = {}


laCats = []
sCount = 0
for x in cats:
    standardDeviationDict[x] = 0

# places standard deviation stats into dictionary
with open('Standard-Deviation-Data') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 0:
            for c in row:
                standardDeviationDict[c] = 0
                laCats.append(c)
        if count == 1:
            for v in row:
                standardDeviationDict[laCats[sCount]] = v
                sCount += 1
        count += 1