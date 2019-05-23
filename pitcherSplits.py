from pitcher_dictionary import *
import requests
from bs4 import BeautifulSoup
import pandas as pd
from player_ID_dict import *
import csv
from pitcherIDs import *
import time

# https://www.fangraphs.com/statsplits.aspx?playerid=10131&position=P&season=0&split=0.2

standardCatList = ['wOBA']
advancedCatList = ['K%', 'BB%', 'BABIP']
bbCatList = ['GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%']
allCatsList = ['wOBA', 'K%', 'BB%', 'BABIP', 'GB%', 'FB%', 'HR/FB', 'Soft%', 'Hard%']

yearList = []
yearList.append('2019')
yearList.append('2018')
yearList.append('2017')
yearList.append('2016')


pitcherDictLHB = {}
pitcherDictRHB = {}

splitCats = ['']

for pitcher in pitcherList:
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

for pitcher in pitcherList:
    start = time.time()
    pitcherID = playerIdsdict[pitcher]
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
            if row[0] == '2017':
                pitcherDictLHB[pitcher]['2017']['wOBA'] = row[1]
            if row[0] == '2016':
                pitcherDictLHB[pitcher]['2016']['wOBA'] = row[1]

    # advanced Scrape
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Columns of chart to be scraped
    columns = ['Season', 'vs L', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP', 'LOB%',
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
            if row[0] == '2017':
                pitcherDictLHB[pitcher]['2017'][advancedCatList[0]] = row[1]
                pitcherDictLHB[pitcher]['2017'][advancedCatList[1]] = row[2]
                pitcherDictLHB[pitcher]['2017'][advancedCatList[2]] = row[3]
            if row[0] == '2016':
                pitcherDictLHB[pitcher]['2016'][advancedCatList[0]] = row[1]
                pitcherDictLHB[pitcher]['2016'][advancedCatList[1]] = row[2]
                pitcherDictLHB[pitcher]['2016'][advancedCatList[2]] = row[3]

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
            if row[0] == '2017':
                pitcherDictLHB[pitcher]['2017'][bbCatList[0]] = row[1]
                pitcherDictLHB[pitcher]['2017'][bbCatList[1]] = row[2]
                pitcherDictLHB[pitcher]['2017'][bbCatList[2]] = row[3]
                pitcherDictLHB[pitcher]['2017'][bbCatList[3]] = row[4]
                pitcherDictLHB[pitcher]['2017'][bbCatList[4]] = row[5]

            if row[0] == '2016':
                pitcherDictLHB[pitcher]['2016'][bbCatList[0]] = row[1]
                pitcherDictLHB[pitcher]['2016'][bbCatList[1]] = row[2]
                pitcherDictLHB[pitcher]['2016'][bbCatList[2]] = row[3]
                pitcherDictLHB[pitcher]['2016'][bbCatList[3]] = row[4]
                pitcherDictLHB[pitcher]['2016'][bbCatList[4]] = row[5]
    end = time.time()
    #print(end - start)

for pitcher in pitcherList:
    start = time.time()
    pitcherID = playerIdsdict[pitcher]
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
            if row[0] == '2017':
                pitcherDictRHB[pitcher]['2017']['wOBA'] = row[1]
            if row[0] == '2016':
                pitcherDictRHB[pitcher]['2016']['wOBA'] = row[1]

    # advanced Scrape
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Columns of chart to be scraped
    columns = ['Season', 'vs L', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP', 'LOB%',
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
            if row[0] == '2017':
                pitcherDictRHB[pitcher]['2017'][advancedCatList[0]] = row[1]
                pitcherDictRHB[pitcher]['2017'][advancedCatList[1]] = row[2]
                pitcherDictRHB[pitcher]['2017'][advancedCatList[2]] = row[3]
            if row[0] == '2016':
                pitcherDictRHB[pitcher]['2016'][advancedCatList[0]] = row[1]
                pitcherDictRHB[pitcher]['2016'][advancedCatList[1]] = row[2]
                pitcherDictRHB[pitcher]['2016'][advancedCatList[2]] = row[3]

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
            if row[0] == '2017':
                pitcherDictRHB[pitcher]['2017'][bbCatList[0]] = row[1]
                pitcherDictRHB[pitcher]['2017'][bbCatList[1]] = row[2]
                pitcherDictRHB[pitcher]['2017'][bbCatList[2]] = row[3]
                pitcherDictRHB[pitcher]['2017'][bbCatList[3]] = row[4]
                pitcherDictRHB[pitcher]['2017'][bbCatList[4]] = row[5]

            if row[0] == '2016':
                pitcherDictRHB[pitcher]['2016'][bbCatList[0]] = row[1]
                pitcherDictRHB[pitcher]['2016'][bbCatList[1]] = row[2]
                pitcherDictRHB[pitcher]['2016'][bbCatList[2]] = row[3]
                pitcherDictRHB[pitcher]['2016'][bbCatList[3]] = row[4]
                pitcherDictRHB[pitcher]['2016'][bbCatList[4]] = row[5]
    end = time.time()
    #print(end - start)
print(pitcherDictLHB)
print(pitcherDictRHB)









































