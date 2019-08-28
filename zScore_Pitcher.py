from global_variables import *


def set_zscores():
    zScorePitcherDict = {}

    for pitcher in startingPitchers:
        zScorePitcherDict[pitcher] = {}

    for pitcher in zScorePitcherDict:
        for year in yearList:
            zScorePitcherDict[pitcher][year] = {}

    for pitcher in zScorePitcherDict:
        for year in yearList:
            for cat in allCatsList:
                zScorePitcherDict[pitcher][year][cat] = 'NTF'

    # print(zScorePitcherDict)
    #
    # print(float(pitcherDict['Mike Minor']['K%']))
    # print(float(lasDict18['K%']))
    # print(float(standardDeviationDict['K%']))
    # zScore = (float(pitcherDict['Mike Minor']['K%']) - float(lasDict18['K%'])) / float(standardDeviationDict['K%'])
    # print(zScore)

    for pitcher in startingPitchers:
        for year in yearList:
            for cat in zScoreCatList:
                print(pitcher, year, cat)
                print('pitcher', cat, pitcherDict[pitcher][year][cat])
                print('las', cat, lasDict18[cat])
                print('std', cat, standardDeviationDict[cat])
                print('--------------')
                if pitcherDict[pitcher][year][cat] != 'NTF':
                    zScorePitcherDict[pitcher][year][cat] = (float(pitcherDict[pitcher][year][cat]) - float(
                        lasDict18[cat])) / (standardDeviationDict[cat])
                else:
                    zScorePitcherDict[pitcher][year][cat] = "NTF"

    for pitcher in zScorePitcherDict:
        for year in yearList:
            for cat in allCatsList:
                if zScorePitcherDict[pitcher][year][cat] != 'NTF':
                    zScorePitcherDict[pitcher][year][cat] = float(zScorePitcherDict[pitcher][year][cat])