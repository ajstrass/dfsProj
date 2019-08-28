import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from global_variables import *

# fills pitcher dictionary with stats

# https://www.fangraphs.com/statss.aspx?playerid=14875&position=P

def set_pitcherDict():
    dashboardCatList = ['HR/FB']
    standardCatList = ['IP']
    advancedCatList = ['K%', 'BB%', 'BABIP']
    bbCatList = ['GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%', 'SIERA']
    zScoreCatList = ['K%', 'BB%', 'GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%', 'SIERA']
    pitcherRatingCatList = ['K%', 'BB%', 'GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%', 'SIERA']
    allCatsList = ['IP', 'K%', 'BB%', 'BABIP', 'GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%', 'SIERA']

    with open('Starting Pitchers') as file:
        reader = csv.reader(file)
        for row in reader:
            startingPitchers.append(row[0])
    startingPitchers.pop(0)

    pitcherDict = {}

    for pitcher in startingPitchers:
        pitcherDict[pitcher] = {}

    for pitcher in pitcherDict:
        for year in yearList:
            pitcherDict[pitcher][year] = {}

    for pitcher in pitcherDict:
        for year in yearList:
            for cat in allCatsList:
                pitcherDict[pitcher][year][cat] = 'NTF'
    x = 0
    for pitcher in startingPitchers:
        if x == 1:
            break
        x = 1
        start = time.time()
        pitcherID = playerIdsdict[pitcher]
        URL = 'https://www.fangraphs.com/statss.aspx?playerid=' + pitcherID + '&position=P'
        print(URL)
        # standard Scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'Team', 'W', 'L', 'ERA', 'G', 'GS', 'CG', 'ShO', 'SV', 'HLD', 'BS', 'IP', 'TBF',
                   'H', 'R', 'ER', 'HR', 'BB', 'IBB', 'HBP', 'WP', 'BK', 'SO']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable', 'id': 'SeasonStats1_dgSeason1_ctl00'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['W', 'L', 'ERA', 'G', 'GS', 'CG', 'ShO', 'SV', 'HLD', 'BS', 'TBF',
                              'H', 'R', 'ER', 'HR', 'BB', 'IBB', 'HBP', 'WP', 'BK', 'SO'])
        df.to_csv('pitcherDict2', index=False)

        with open('pitcherDict2') as file:
            changes = []
            final = []
            reader = csv.reader(file)
            for row in reader:
                changes.append(row)
            count = 0
            for row in changes:
                if '(A' in row[1]:
                    changes[count][0] = '--'
                if 'Average' in row[1]:
                    changes[count][0] = '--'

                if '(R' in row[1]:
                    changes[count][0] = '--'
                if 'THE BAT' in row[1]:
                    changes[count][0] = '--'
                if 'Steamer' in row[1]:
                    changes[count][0] = '--'
                if 'Depth' in row[1]:
                    changes[count][0] = '--'
                if 'ATC' in row[1]:
                    changes[count][0] = '--'
                if '(' in row[1]:
                    changes[count][0] = '--'
                if 'Zi' in row[1]:
                    changes[count][0] = '--'
                count += 1

            sixList = []
            sevenList = []
            eightList = []
            nineList = []
            rowCount = 0
            for row in changes:
                if row[0] == '2016':
                    sixList.append(('2016', row[2], rowCount))
                if row[0] == '2017':
                    sevenList.append(('2017', row[2], rowCount))
                if row[0] == '2018':
                    eightList.append(('2018', row[2], rowCount))
                if row[0] == '2019':
                    nineList.append(('2019', row[2], rowCount))
                rowCount += 1

            if len(sixList) > 1:
                if float(sixList[0][1]) > float(sixList[1][1]):
                    sixList.pop(1)
                elif float(sixList[1][1]) > float(sixList[0][1]):
                    sixList.pop(0)

            if len(sevenList) > 1:
                if float(sevenList[0][1]) > float(sevenList[1][1]):
                    sevenList.pop(1)
                elif float(sevenList[1][1]) > float(sevenList[0][1]):
                    sevenList.pop(0)

            if len(eightList) > 1:
                if float(eightList[0][1]) > float(eightList[1][1]):
                    eightList.pop(1)
                elif float(eightList[1][1]) > float(eightList[0][1]):
                    eightList.pop(0)

            if len(nineList) > 1:
                if float(nineList[0][1]) > float(nineList[1][1]):
                    nineList.pop(1)
                elif float(nineList[1][1]) > float(nineList[0][1]):
                    nineList.pop(0)
            rowIndexes = []
            if len(sixList) > 0:
                rowIndexes.append(sixList[0][2])
            if len(sevenList) > 0:
                rowIndexes.append(sevenList[0][2])
            if len(eightList) > 0:
                rowIndexes.append(eightList[0][2])
            if len(nineList) > 0:
                rowIndexes.append(nineList[0][2])
            rowIndexes.sort()
            rowIndexes1 = []
            rowIndexes2 = []
            rowIndexes3 = []
            for num in rowIndexes:
                rowIndexes1.append(num)
                rowIndexes2.append(num)
                rowIndexes3.append(num)

            with open('pitcherDict2') as file1:
                reader = csv.reader(file1)
                r = 0
                for row in reader:
                    if len(rowIndexes1) > 0:
                        if r == rowIndexes1[0]:
                            final.append(row)
                            rowIndexes1.pop(0)
                    r += 1

            for row in final:
                if row[0] == '2019':
                    pitcherDict[pitcher]['2019'][standardCatList[0]] = row[2]

                if row[0] == '2018':
                    pitcherDict[pitcher]['2018'][standardCatList[0]] = row[2]

                if row[0] == '2017':
                    pitcherDict[pitcher]['2017'][standardCatList[0]] = row[2]

                if row[0] == '2016':
                    pitcherDict[pitcher]['2016'][standardCatList[0]] = row[2]

        # advanced Scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'Team', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP',
                   'LOB%',
                   'ERA-', 'FIP-', 'FIP']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable', 'id': 'SeasonStats1_dgSeason2_ctl00'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['K/9', 'BB/9', 'K/BB', 'HR/9', 'K-BB%', 'AVG', 'WHIP', 'LOB%',
                              'ERA-', 'FIP-', 'FIP'])
        df.to_csv('pitcherDict', index=False)

        with open('pitcherDict') as file:
            changes = []
            final = []
            reader = csv.reader(file)
            for row in reader:
                if row[1] != 'Average':
                    changes.append(row)
            count = 0
            for row in changes:
                if '(A' in row[1]:
                    changes[count][0] = '--'
                if 'Average' in row[1]:
                    changes[count][0] = '--'

                if '(R' in row[1]:
                    changes[count][0] = '--'
                if 'THE BAT' in row[1]:
                    changes[count][0] = '--'
                if 'Steamer' in row[1]:
                    changes[count][0] = '--'
                if 'Depth' in row[1]:
                    changes[count][0] = '--'
                if 'ATC' in row[1]:
                    changes[count][0] = '--'
                if '(' in row[1]:
                    changes[count][0] = '--'
                if 'Zi' in row[1]:
                    changes[count][0] = '--'
                if 'Average' in row[1]:
                    changes[count][0] = '--'
                count += 1
            r = 0
            for row in changes:
                if len(rowIndexes2) > 0:
                    if r == rowIndexes2[0]:
                        final.append(row)
                        rowIndexes2.pop(0)
                r += 1

            for row in final:
                if row[0] == '2019':
                    pitcherDict[pitcher]['2019'][advancedCatList[0]] = row[2]
                    pitcherDict[pitcher]['2019'][advancedCatList[1]] = row[3]
                    pitcherDict[pitcher]['2019'][advancedCatList[2]] = row[4]
                if row[0] == '2018':
                    pitcherDict[pitcher]['2018'][advancedCatList[0]] = row[2]
                    pitcherDict[pitcher]['2018'][advancedCatList[1]] = row[3]
                    pitcherDict[pitcher]['2018'][advancedCatList[2]] = row[4]
                if row[0] == '2017':
                    pitcherDict[pitcher]['2017'][advancedCatList[0]] = row[2]
                    pitcherDict[pitcher]['2017'][advancedCatList[1]] = row[3]
                    pitcherDict[pitcher]['2017'][advancedCatList[2]] = row[4]
                if row[0] == '2016':
                    pitcherDict[pitcher]['2016'][advancedCatList[0]] = row[2]
                    pitcherDict[pitcher]['2016'][advancedCatList[1]] = row[3]
                    pitcherDict[pitcher]['2016'][advancedCatList[2]] = row[4]

        # battedball Scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'Team', 'GB/FB', 'LD%', 'GB%', 'FB%', 'IFFB%', 'HR/FB', 'IFH%', 'BUH%', 'Pull%',
                   'Cent%', 'Oppo%', 'Soft%', 'Med%', 'Hard%', 'SIERA', 'xFIP-', 'xFIP']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable', 'id': 'SeasonStats1_dgSeason3_ctl00'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['GB/FB', 'LD%', 'IFFB%', 'IFH%', 'BUH%', 'Pull%',
                              'Cent%', 'Oppo%', 'Med%', 'xFIP-', 'xFIP'])
        df.to_csv('pitcherDict1', index=False)

        with open('pitcherDict1') as file:
            changes = []
            final = []
            reader = csv.reader(file)
            for row in reader:
                changes.append(row)
            count = 0
            for row in changes:
                if '(A' in row[1]:
                    changes[count][0] = '--'
                if 'Average' in row[1]:
                    changes[count][0] = '--'

                if '(R' in row[1]:
                    changes[count][0] = '--'
                if 'THE BAT' in row[1]:
                    changes[count][0] = '--'
                if 'Steamer' in row[1]:
                    changes[count][0] = '--'
                if 'Depth' in row[1]:
                    changes[count][0] = '--'
                if 'ATC' in row[1]:
                    changes[count][0] = '--'
                if '(' in row[1]:
                    changes[count][0] = '--'
                if 'Zi' in row[1]:
                    changes[count][0] = '--'
                if row[5] == '\xa0':
                    changes[count][0] = '--'
                count += 1
            r = 0
            for row in changes:
                if row[0] == '2019':
                    final.append(row)
                if row[0] == '2018':
                    final.append(row)
                if row[0] == '2017':
                    final.append(row)
                if row[0] == '2016':
                    final.append(row)

            for row in final:
                if row[0] == '2019':
                    pitcherDict[pitcher]['2019'][bbCatList[0]] = row[2]
                    pitcherDict[pitcher]['2019'][bbCatList[1]] = row[3]
                    pitcherDict[pitcher]['2019'][bbCatList[2]] = row[4]
                    pitcherDict[pitcher]['2019'][bbCatList[3]] = row[5]
                    pitcherDict[pitcher]['2019'][bbCatList[4]] = row[6]
                    pitcherDict[pitcher]['2019'][bbCatList[5]] = row[7]
                if row[0] == '2018':
                    pitcherDict[pitcher]['2018'][bbCatList[0]] = row[2]
                    pitcherDict[pitcher]['2018'][bbCatList[1]] = row[3]
                    pitcherDict[pitcher]['2018'][bbCatList[2]] = row[4]
                    pitcherDict[pitcher]['2018'][bbCatList[3]] = row[5]
                    pitcherDict[pitcher]['2018'][bbCatList[4]] = row[6]
                    pitcherDict[pitcher]['2018'][bbCatList[5]] = row[7]
                if row[0] == '2017':
                    pitcherDict[pitcher]['2017'][bbCatList[0]] = row[2]
                    pitcherDict[pitcher]['2017'][bbCatList[1]] = row[3]
                    pitcherDict[pitcher]['2017'][bbCatList[2]] = row[4]
                    pitcherDict[pitcher]['2017'][bbCatList[3]] = row[5]
                    pitcherDict[pitcher]['2017'][bbCatList[4]] = row[6]
                    pitcherDict[pitcher]['2017'][bbCatList[5]] = row[7]
                if row[0] == '2016':
                    pitcherDict[pitcher]['2016'][bbCatList[0]] = row[2]
                    pitcherDict[pitcher]['2016'][bbCatList[1]] = row[3]
                    pitcherDict[pitcher]['2016'][bbCatList[2]] = row[4]
                    pitcherDict[pitcher]['2016'][bbCatList[3]] = row[5]
                    pitcherDict[pitcher]['2016'][bbCatList[4]] = row[6]
                    pitcherDict[pitcher]['2016'][bbCatList[5]] = row[7]

        end = time.time()

    for pitcher in pitcherDict:
        for year in yearList:
            for cat in allCatsList:
                if ' %' in pitcherDict[pitcher][year][cat]:
                    pitcherDict[pitcher][year][cat] = pitcherDict[pitcher][year][cat].strip(' %')
                if pitcherDict[pitcher][year][cat] != 'NTF':
                    pitcherDict[pitcher][year][cat] = float(pitcherDict[pitcher][year][cat])


