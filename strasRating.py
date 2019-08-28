pitcherValueDict = {}
from global_variables import *

def set_pitcherRankings():
    categories = ['K%', 'BB%', 'GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%', 'SIERA']
    pitcherValueDict = {}

    for pitcher in startingPitchers:
        pitcherValueDict[pitcher] = {}

    for pitcher in pitcherValueDict:
        for year in yearList:
            pitcherValueDict[pitcher][year] = 'NTF'
        pitcherValueDict[pitcher]["TOTAL"] = 'NTF'

    for pitcher in startingPitchers:
        for year in yearList:
            netPos = 0
            netNeg = 0
            if pitcherDict[pitcher][year]['IP'] != 'NTF':
                if pitcherDict[pitcher][year]['IP'] > 50:
                    netPos = (zScorePitcherDict[pitcher][year]['K%'] * 1.75) + (
                                zScorePitcherDict[pitcher][year]['GB%'] * .5) \
                             + (zScorePitcherDict[pitcher][year]['Soft%'] * .5)
                    netNeg = (zScorePitcherDict[pitcher][year]['BB%'] * -1.5) + (
                                zScorePitcherDict[pitcher][year]['FB%'] * -0.5) \
                             + (zScorePitcherDict[pitcher][year]['Hard%'] * -0.5) + (
                                         zScorePitcherDict[pitcher][year]['SIERA'] * -2)
                    pitcherValueDict[pitcher][year] = netPos + netNeg

    for pitcher in startingPitchers:
        sumList = []
        yearsPlayed = 0
        y1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        totalVal = 0
        if pitcherValueDict[pitcher]['2019'] != 'NTF':
            y1 = pitcherValueDict[pitcher]['2019']
            yearsPlayed += 1
            sumList.append((y1))
        if pitcherValueDict[pitcher]['2018'] != 'NTF':
            y2 = pitcherValueDict[pitcher]['2018']
            yearsPlayed += 1
            sumList.append((y2))
        if pitcherValueDict[pitcher]['2017'] != 'NTF':
            y3 = pitcherValueDict[pitcher]['2017']
            yearsPlayed += 1
            sumList.append(y3)
        # if pitcherValueDict[pitcher]['2016'] != 'NTF':
        #     y4 = pitcherValueDict[pitcher]['2016']
        #     yearsPlayed += 1
        #     sumList.append(y4)
        if y1 != 0 and y2 != 0 and y3 != 0:
            totalVal = (y1 * .75) + (y2 * .2) + (y3 * .05)
            pitcherValueDict[pitcher]['TOTAL'] = totalVal
        elif y1 != 0 and y2 != 0 and y3 == 0:
            totalVal = (y1 * .80) + (y2 * .2)
            pitcherValueDict[pitcher]['TOTAL'] = totalVal
        elif y1 != 0 and y2 == 0 and y3 == 0:
            totalVal = y1
            pitcherValueDict[pitcher]['TOTAL'] = totalVal
        elif y1 == 0 and y2 != 0 and y3 != 0:
            totalVal = (y2 * .80) + (y3 * .20)
            pitcherValueDict[pitcher]['TOTAL'] = totalVal
        else:
            pitcherValueDict[pitcher]['TOTAL'] = -100  # not enough data

    orderedPitchers = []

    for pitcher in pitcherValueDict:
        orderedPitchers.append((pitcher, pitcherValueDict[pitcher]['TOTAL']))
    orderedPitchers.sort(key=lambda tup: tup[1])




