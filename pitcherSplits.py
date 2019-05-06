from pitcher_dictionary import *
import requests
from bs4 import BeautifulSoup
import pandas as pd
from player_ID_dict import *
from battersDict import *
import csv
from pitcherIDs import *


# https://www.fangraphs.com/statsplits.aspx?playerid=10131&position=P&season=0&split=0.2

pitcherDictLHB = {}
pitcherDictRHB = {}

for pitcher in pitcherList:
    pitcherDictLHB[pitcher] = {}
    pitcherDictRHB[pitcher] = {}

pitcherID = 0

pitcherID = playerIdsdict['Matt Harvey']

# Scrape data vs LHB
# Standard Data
URL = 'https://www.fangraphs.com/statsplits.aspx?playerid='+pitcherID+'&position=P&season=0&split=0.1'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['Season', 'vs L', 'IP', 'ERA', 'TBF', 'H', '2B', '3B', 'R', 'ER', 'HR', 'BB',
           'IBB', 'HBP', 'SO', 'AVG', 'OBP', 'SLG', 'wOBA']
# creates frame of table
df = pd.DataFrame(columns=columns)
# finds table from website
table = soup.find('table', attrs={'class':'rgMasterTable'}).tbody
# parses table to get data
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)
# converts data frame to csv
df = df.drop(columns=['vs L', 'ERA', 'TBF', 'H', '2B', '3B', 'R', 'ER', 'HR', 'BB',
           'IBB', 'HBP', 'SLG'])
df.to_csv('pitcherSplitsLHB', index=False)

with open('pitcherSplitsLHB') as file:
    reader = csv.reader(file)
    for row in reader:
        pitcherDictLHB['Matt Harvey'][row[0]] = row

# Advanced Data
URL = 'https://www.fangraphs.com/statsplits.aspx?playerid='+pitcherID+'&position=P&season=0&split=0.1'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['Season', 'vs L', 'K/9',	'BB/9',	'K/BB',	'HR/9',	'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP', 'LOB%', 'FIP', 'xFIP']
# creates frame of table
df = pd.DataFrame(columns=columns)
# finds table from website
table = soup.find('table', attrs={'id':'SeasonSplits1_dgSeason2_ctl00'}).tbody
# parses table to get data
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)
# converts data frame to csv
df = df.drop(columns=[])
df.to_csv('pitcherSplitsLHB', index=False)

with open('pitcherSplitsLHB') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count < 1:
            count += 1
            for x in row:
                "assa"


print(pitcherDictLHB)