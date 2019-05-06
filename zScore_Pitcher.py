from rStats import *
from Standard_Deviation import *

zScorePitcherDict = {}

categories = []

for pitcher in pitcherDict:
    zScorePitcherDict[pitcher] = {}
    for category in pitcherDict[pitcher]:
        zScorePitcherDict[pitcher][category] = 0
        if category not in categories:
            categories.append(category)
categories.remove('Name')
categories.remove('Team')
categories.remove('SV')
categories.remove('L')
categories.remove('G')
categories.remove('GS')
categories.remove('WAR')
categories.remove('IP')
categories.remove('LOB%')


# print(zScorePitcherDict)
#
# print(float(pitcherDict['Mike Minor']['K%']))
# print(float(lasDict18['K%']))
# print(float(standardDeviationDict['K%']))
# zScore = (float(pitcherDict['Mike Minor']['K%']) - float(lasDict18['K%'])) / float(standardDeviationDict['K%'])
# print(zScore)

for pitcher in pitcherDict:
    for category in categories:
        if float(standardDeviationDict[category]) != 0:
            zScore = (float(pitcherDict[pitcher][category]) - float(lasDict18[category])) / float(standardDeviationDict[category])
        else:
            zScore = 1
        zScorePitcherDict[pitcher][category] = zScore

# print(zScorePitcherDict['Mike Minor'])
