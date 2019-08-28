import csv
import requests
import pandas as pd
import pickle as pickle
from bs4 import BeautifulSoup
from global_variables import *

def get_csv():
    dls = "https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=8&season=2019&month=0&season1=2019&ind=0&team=0&rost=0&age=0&filter=&players=p2019-7-23&page=1_50 FanGraphs Leaderboard.csv"
    resp = requests.get(dls)

    output = open('testSP.csv', 'wb')
    output.write(resp.content)
    output.close()

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def show_label(self, event=None):
    self.label.lift(self.frame)

def hide_label(self, event=None):
    self.label.lower(self.frame)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def get_pitcherIDS():
    data = requests.get('http://crunchtimebaseball.com/master.csv')
    with open('playerIdCsv.csv', 'w') as f:
        writer = csv.writer(f)
        reader = csv.reader(data.text.splitlines())
        # reads file line by line
        rowNum = 0
        for row in reader:
            # writes file to lineup data
            writer.writerow(row)

def set_pitcherIDS():
    pitcherIdsdict = {}

    with open('playerIdCsv.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            for col in row:
                pitcherIdsdict[row[18]] = row[17]

    pitcherIdsdict['Griffin Canning'] = '19867'

    save_obj(pitcherIdsdict, 'pitcherIdsdict')

def set_batterIDS():
    batterIDSDict = {}

    with open('player-ids') as file:
        rowNum = 0
        reader = csv.reader(file)
        for row in reader:
            # skips first row
            if rowNum == 0:
                rowNum += 1
                # col by col adds batter to each list
                for pid in row:
                    batterIDSDict[pid] = 0
                    batterList.append(pid)
            else:
                # col by col adds id to list
                for pid in row:
                    idList.append(pid)

    # combines 2 lists to Dictionary
    batterIDSDict = dict(zip(batterList, idList))

    save_obj(batterIDSDict, 'batterIDSDict')

def get_datascrape(month, day, year):
    if month == '':
        return
    startersList = []

    # user inputs date
    month = month
    day = day
    year = year
    startingPitchers = []
    print('Gathering Data for', month, '-', day, '-', year)
    # Custom URL to set the user entered day
    URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=8&season=' + year + '&month=0&season1=' + year + '&ind=0&team=0&rost=0&age=0&filter=&players=p' + year + '-' + month + '-' + day + '&page=1_50'
    print(URL)
    # start scrape
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Columns of chart to be scraped
    columns = ['#', 'Name', 'Team', 'W', 'L', 'SV', 'G', 'GS', 'IP', 'K/9', 'BB/9',
               'HR/9', 'BABIP', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP', 'WAR']
    # creates frame of table
    df = pd.DataFrame(columns=columns)
    # finds table from website
    table = soup.find('table', attrs={'class': 'rgMasterTable'}).tbody
    # parses table to get data
    trs = table.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        row = [td.text.replace('\n', '') for td in tds]
        df = df.append(pd.Series(row, index=columns), ignore_index=True)
    # converts data frame to csv
    df = df.drop(columns=['#', 'Team', 'W', 'L', 'SV', 'G', 'GS', 'IP', 'K/9', 'BB/9',
                          'HR/9', 'BABIP', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP', 'WAR'])
    df = df.sort_values('Name')
    df.to_csv('Starting Pitchers', index=False)

    with open('Starting Pitchers') as file:
        reader = csv.reader(file)
        for pitcher in reader:
            startersList.append(pitcher)

    print('dsf')
    save_obj(startersList, 'startersList')


def set_pitcherDict():
    pitcherDict = load_obj('pitcherDict')
    pitcherIdsdict = load_obj('pitcherIdsdict')

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

    set_pitcherIDS()

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
            ''#break
        x = 1
        pitcherID = pitcherIdsdict[pitcher]
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


    for pitcher in pitcherDict:
        for year in yearList:
            for cat in allCatsList:
                if ' %' in pitcherDict[pitcher][year][cat]:
                    pitcherDict[pitcher][year][cat] = pitcherDict[pitcher][year][cat].strip(' %')
                if pitcherDict[pitcher][year][cat] != 'NTF':
                    pitcherDict[pitcher][year][cat] = float(pitcherDict[pitcher][year][cat])

    save_obj(pitcherDict, 'pitcherDict')

def set_las():


    lasDict19 = {}
    lasDict18 = {}

    for x in allCatsList:
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
                    v = v.rstrip('%')
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
                    v = v.rstrip('%')
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
                    v = v.rstrip('%')
                    lasDict19[laCats[sCount]] = float(v)
                    sCount += 1
            count += 1

    # places 2019 advanced stats into dictionary
    with open('LA-AdvancedStats-2018') as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            if count == 0:
                for c in row:
                    lasDict18[c] = 0
                    laCats.append(c)
            if count == 1:
                for v in row:
                    v = v.rstrip('%')
                    lasDict18[laCats[sCount]] = float(v)
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
                    v = v.rstrip('%')
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
                    v = v.rstrip('%')
                    lasDict18[laCats[sCount]] = float(v)
                    sCount += 1
            count += 1
    save_obj(lasDict18, 'lasDict18')
    save_obj(lasDict19, 'lasDict19')

def set_sdd():
    standardDeviationDict = {}
    catsList = ['IP', 'K/9', 'BB/9', 'HR/9', 'BABIP', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP',
                'xFIP', 'WAR', 'K/BB', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'ERA-', 'FIP-', 'xFIP-'
        , 'E-F', 'SIERA', 'BABIP', 'GB/FB', 'LD%', 'GB%', 'FB%', 'IFFB%', 'HR/FB', 'RS', 'RS/9', 'Balls ',
                'Strikes', 'Pitches', 'Pull%', 'Cent%', 'Oppo%', 'Soft%', 'Med%', 'Hard%']
    laCats = []
    sCount = 0
    for x in catsList:
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
                    standardDeviationDict[laCats[sCount]] = float(v[1:])
                    sCount += 1

            count += 1
    save_obj(standardDeviationDict, 'standardDeviationDict')

def set_zscores():


    pitcherDict = load_obj('pitcherDict')
    lasDict18 = load_obj('lasDict18')
    standardDeviationDict = load_obj('standardDeviationDict')

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

    for pitcher in startingPitchers:
        for year in yearList:
            for cat in zScoreCatList:
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
    save_obj(zScorePitcherDict, 'zScorePitcherDict')

def set_pitcherSkill():


    pitcherDict = load_obj('pitcherDict')
    lasDict18 = load_obj('lasDict18')
    standardDeviationDict = load_obj('standardDeviationDict')
    zScorePitcherDict = load_obj('zScorePitcherDict')

    categories = ['K%', 'BB%', 'GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%', 'SIERA']
    pitcherSkillDict = {}

    for pitcher in startingPitchers:
        pitcherSkillDict[pitcher] = {}

    for pitcher in pitcherSkillDict:
        for year in yearList:
            pitcherSkillDict[pitcher][year] = 'NTF'
        pitcherSkillDict[pitcher]["TOTAL"] = 'NTF'

    for pitcher in startingPitchers:
        for year in yearList:
            netPos = 0
            netNeg = 0
            if pitcherDict[pitcher][year]['IP'] != 'NTF':
                if pitcherDict[pitcher][year]['IP'] > 14:
                    netPos = (zScorePitcherDict[pitcher][year]['K%'] * 2) + (
                            zScorePitcherDict[pitcher][year]['GB%'] * .5) \
                             + (zScorePitcherDict[pitcher][year]['Soft%'] * .5)
                    netNeg = (zScorePitcherDict[pitcher][year]['BB%'] * -1) + (
                            zScorePitcherDict[pitcher][year]['FB%'] * -0.5) \
                             + (zScorePitcherDict[pitcher][year]['Hard%'] * -1) + (
                                     zScorePitcherDict[pitcher][year]['SIERA'] * -2.5)
                    pitcherSkillDict[pitcher][year] = netPos + netNeg

    for pitcher in startingPitchers:
        sumList = []
        yearsPlayed = 0
        y1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        totalVal = 0
        if pitcherSkillDict[pitcher]['2019'] != 'NTF':
            y1 = pitcherSkillDict[pitcher]['2019']
            yearsPlayed += 1
            sumList.append((y1))
        if pitcherSkillDict[pitcher]['2018'] != 'NTF':
            y2 = pitcherSkillDict[pitcher]['2018']
            yearsPlayed += 1
            sumList.append((y2))
        if pitcherSkillDict[pitcher]['2017'] != 'NTF':
            y3 = pitcherSkillDict[pitcher]['2017']
            yearsPlayed += 1
            sumList.append(y3)
        # if pitcherSkillDict[pitcher]['2016'] != 'NTF':
        #     y4 = pitcherSkillDict[pitcher]['2016']
        #     yearsPlayed += 1
        #     sumList.append(y4)
        if y1 != 0 and y2 != 0:
            totalVal = ((y1 * .75) + (y2 * .25))
            pitcherSkillDict[pitcher]['TOTAL'] = totalVal
        elif y1 != 0 and y2 == 0:
            totalVal = y1
            pitcherSkillDict[pitcher]['TOTAL'] = totalVal
        elif y1 == 0 and y2 != 0:
            totalVal = y2
            pitcherSkillDict[pitcher]['TOTAL'] = totalVal
        else:
            pitcherSkillDict[pitcher]['TOTAL'] = -100  # not enough data

    save_obj(pitcherSkillDict, 'pitcherSkillDict')

def set_pitcherSplits():
    # https://www.fangraphs.com/statsplits.aspx?playerid=10131&position=P&season=0&split=0.2

    pitcherDict = load_obj('pitcherDict')
    lasDict18 = load_obj('lasDict18')
    standardDeviationDict = load_obj('standardDeviationDict')
    zScorePitcherDict = load_obj('zScorePitcherDict')
    pitcherIdsdict = load_obj('pitcherIdsdict')

    standardCatList = ['wOBA']
    advancedCatList = ['K%', 'BB%', 'BABIP']
    bbCatList = ['GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%']
    allCatsList = ['wOBA', 'K%', 'BB%', 'BABIP', 'GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%']

    yearList = []
    yearList.append('2019')
    yearList.append('2018')

    pitcherDictLHB = {}
    pitcherDictRHB = {}

    splitCats = ['']

    for pitcher in startingPitchers:
        pitcherDictLHB[pitcher] = {}
        pitcherDictRHB[pitcher] = {}

    for pitcher in pitcherDictLHB:
        for year in yearList:
            pitcherDictLHB[pitcher][year] = {}
            pitcherDictRHB[pitcher][year] = {}

    for pitcher in pitcherDictLHB:
        for year in yearList:
            for cat in allCatsList:
                pitcherDictLHB[pitcher][year][cat] = 'NTF'
                pitcherDictRHB[pitcher][year][cat] = 'NTF'

    for pitcher in startingPitchers:
        pitcherID = pitcherIdsdict[pitcher]
        URL = 'https://www.fangraphs.com/statsplits.aspx?playerid=' + pitcherID + '&position=P&season=0&split=0.1'
        # standardScrape
        ######################
        # start scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'vs L', 'IP', 'ERA', 'TBF', 'H', '2B', '3B', 'R', 'ER', 'HR', 'BB',
                   'IBB', 'HBP', 'SO', 'AVG', 'OBP', 'SLG', 'wOBA']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['vs L', 'IP', 'ERA', 'TBF', 'H', '2B', '3B', 'R', 'ER', 'HR', 'BB',
                              'IBB', 'HBP', 'SO', 'AVG', 'OBP', 'SLG'])
        df.to_csv('pitcherSplitsLHB', index=False)

        with open('pitcherSplitsLHB') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == '2019':
                    pitcherDictLHB[pitcher]['2019']['wOBA'] = row[1]
                if row[0] == '2018':
                    pitcherDictLHB[pitcher]['2018']['wOBA'] = row[1]

        # advanced Scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'vs L', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP',
                   'LOB%',
                   'FIP', 'xFIP']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable', 'id': 'SeasonSplits1_dgSeason2_ctl00'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['vs L', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K-BB%', 'AVG', 'WHIP', 'LOB%',
                              'FIP', 'xFIP'])
        df.to_csv('pitcherSplitsLHB', index=False)

        with open('pitcherSplitsLHB') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == '2019':
                    pitcherDictLHB[pitcher]['2019'][advancedCatList[0]] = row[1]
                    pitcherDictLHB[pitcher]['2019'][advancedCatList[1]] = row[2]
                    pitcherDictLHB[pitcher]['2019'][advancedCatList[2]] = row[3]
                if row[0] == '2018':
                    pitcherDictLHB[pitcher]['2018'][advancedCatList[0]] = row[1]
                    pitcherDictLHB[pitcher]['2018'][advancedCatList[1]] = row[2]
                    pitcherDictLHB[pitcher]['2018'][advancedCatList[2]] = row[3]

        # battedball Scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'vs L', 'GB/FB', 'LD%', 'GB%', 'FB%', 'IFFB%', 'HR/FB', 'IFH%', 'BUH%', 'Pull%',
                   'Cent%', 'Oppo%', 'Soft%', 'Med%', 'Hard%', 'Pitches', 'Balls', 'Strikes']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable', 'id': 'SeasonSplits1_dgSeason3_ctl00'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['vs L', 'GB/FB', 'LD%', 'IFFB%', 'IFH%', 'BUH%', 'Pull%',
                              'Cent%', 'Oppo%', 'Med%', 'Pitches', 'Balls', 'Strikes'])
        df.to_csv('pitcherSplitsLHB', index=False)

        with open('pitcherSplitsLHB') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == '2019':
                    pitcherDictLHB[pitcher]['2019'][bbCatList[0]] = row[1]
                    pitcherDictLHB[pitcher]['2019'][bbCatList[1]] = row[2]
                    pitcherDictLHB[pitcher]['2019'][bbCatList[2]] = row[3]
                    pitcherDictLHB[pitcher]['2019'][bbCatList[3]] = row[4]
                    pitcherDictLHB[pitcher]['2019'][bbCatList[4]] = row[5]
                if row[0] == '2018':
                    pitcherDictLHB[pitcher]['2018'][bbCatList[0]] = row[1]
                    pitcherDictLHB[pitcher]['2018'][bbCatList[1]] = row[2]
                    pitcherDictLHB[pitcher]['2018'][bbCatList[2]] = row[3]
                    pitcherDictLHB[pitcher]['2018'][bbCatList[3]] = row[4]
                    pitcherDictLHB[pitcher]['2018'][bbCatList[4]] = row[5]

    for pitcher in startingPitchers:
        pitcherID = pitcherIdsdict[pitcher]
        URL = 'https://www.fangraphs.com/statsplits.aspx?playerid=' + pitcherID + '&position=P&season=0&split=0.2'
        # standardScrape
        ######################
        # start scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'vs L', 'IP', 'ERA', 'TBF', 'H', '2B', '3B', 'R', 'ER', 'HR', 'BB',
                   'IBB', 'HBP', 'SO', 'AVG', 'OBP', 'SLG', 'wOBA']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['vs L', 'IP', 'ERA', 'TBF', 'H', '2B', '3B', 'R', 'ER', 'HR', 'BB',
                              'IBB', 'HBP', 'SO', 'AVG', 'OBP', 'SLG'])
        df.to_csv('pitcherSplitsRHB', index=False)

        with open('pitcherSplitsRHB') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == '2019':
                    pitcherDictRHB[pitcher]['2019']['wOBA'] = row[1]
                if row[0] == '2018':
                    pitcherDictRHB[pitcher]['2018']['wOBA'] = row[1]

        # advanced Scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'vs L', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP',
                   'LOB%',
                   'FIP', 'xFIP']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable', 'id': 'SeasonSplits1_dgSeason2_ctl00'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['vs L', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K-BB%', 'AVG', 'WHIP', 'LOB%',
                              'FIP', 'xFIP'])
        df.to_csv('pitcherSplitsRHB', index=False)

        with open('pitcherSplitsRHB') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == '2019':
                    pitcherDictRHB[pitcher]['2019'][advancedCatList[0]] = row[1]
                    pitcherDictRHB[pitcher]['2019'][advancedCatList[1]] = row[2]
                    pitcherDictRHB[pitcher]['2019'][advancedCatList[2]] = row[3]
                if row[0] == '2018':
                    pitcherDictRHB[pitcher]['2018'][advancedCatList[0]] = row[1]
                    pitcherDictRHB[pitcher]['2018'][advancedCatList[1]] = row[2]
                    pitcherDictRHB[pitcher]['2018'][advancedCatList[2]] = row[3]

        # battedball Scrape
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Columns of chart to be scraped
        columns = ['Season', 'vs L', 'GB/FB', 'LD%', 'GB%', 'FB%', 'IFFB%', 'HR/FB', 'IFH%', 'BUH%', 'Pull%',
                   'Cent%', 'Oppo%', 'Soft%', 'Med%', 'Hard%', 'Pitches', 'Balls', 'Strikes']
        # creates frame of table
        df = pd.DataFrame(columns=columns)
        # finds table from website
        table = soup.find('table', attrs={'class': 'rgMasterTable', 'id': 'SeasonSplits1_dgSeason3_ctl00'}).tbody
        # parses table to get data
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)
        # converts data frame to csv
        df = df.drop(columns=['vs L', 'GB/FB', 'LD%', 'IFFB%', 'IFH%', 'BUH%', 'Pull%',
                              'Cent%', 'Oppo%', 'Med%', 'Pitches', 'Balls', 'Strikes'])
        df.to_csv('pitcherSplitsRHB', index=False)

        with open('pitcherSplitsRHB') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == '2019':
                    pitcherDictRHB[pitcher]['2019'][bbCatList[0]] = row[1]
                    pitcherDictRHB[pitcher]['2019'][bbCatList[1]] = row[2]
                    pitcherDictRHB[pitcher]['2019'][bbCatList[2]] = row[3]
                    pitcherDictRHB[pitcher]['2019'][bbCatList[3]] = row[4]
                    pitcherDictRHB[pitcher]['2019'][bbCatList[4]] = row[5]
                if row[0] == '2018':
                    pitcherDictRHB[pitcher]['2018'][bbCatList[0]] = row[1]
                    pitcherDictRHB[pitcher]['2018'][bbCatList[1]] = row[2]
                    pitcherDictRHB[pitcher]['2018'][bbCatList[2]] = row[3]
                    pitcherDictRHB[pitcher]['2018'][bbCatList[3]] = row[4]
                    pitcherDictRHB[pitcher]['2018'][bbCatList[4]] = row[5]

    save_obj(pitcherDictLHB, 'pitcherDictLHB')
    save_obj(pitcherDictRHB, 'pitcherDictRHB')
    

def print_pitchersRanked():
    pitcherSkillDict = load_obj('pitcherSkillDict')
    orderedPitchers = []

    for pitcher in pitcherSkillDict:
        orderedPitchers.append((pitcher, pitcherSkillDict[pitcher]['TOTAL']))
    orderedPitchers.sort(key=lambda tup: tup[1])
    print(orderedPitchers)