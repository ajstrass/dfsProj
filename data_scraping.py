import requests
from bs4 import BeautifulSoup
import pandas as pd

# user inputs date
month = input('Enter Month \n')
day = input('Enter Day \n')
year = input('Enter Year\n')

print('Gathering Data for',month,'-',day,'-',year)
# Custom URL to set the user entered day
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=8&season='+year+'&month=0&season1='+year+'&ind=0&team=0&rost=0&age=0&filter=&players=p'+year+'-'+month+'-'+day
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
table = soup.find('table', attrs={'class':'rgMasterTable'}).tbody
# parses table to get data
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)
# converts data frame to csv
df = df.drop(columns=['#'])
df = df.sort_values('Name')
df.to_csv('DashboardStats', index=False)


# Scrape advanced data
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=1&season='+year+'&month=0&season1='+year+'&ind=0&team=0&rost=0&age=0&filter=&players=p'+year+'-'+month+'-'+day
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['#', 'Name', 'Team', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP', 'LOB%', 'ERA-', 'FIP-', 'xFIP-', 'ERA', 'FIP', 'E-F', 'xFIP', 'SIERA']
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
df = df.drop(columns=['#', 'Team', 'K/9', 'BB/9', 'HR/9', 'BABIP', 'LOB%', 'ERA', 'FIP', 'xFIP'])
df = df.sort_values('Name')
df.to_csv('AdvancedStats', index=False)


# Scrape BattedBalls data
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=2&season='+year+'&month=0&season1='+year+'&ind=0&team=0&rost=0&age=0&filter=&players=p'+year+'-'+month+'-'+day
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['#', 'Name', 'Team', 'BABIP', 'GB/FB', 'LD%', 'GB%', 'FB%', 'IFFB%', 'HR/FB', 'RS', 'RS/9', 'Balls', 'Strikes', 'Pitches', 'Pull%', 'Cent%', 'Oppo%', 'Soft%', 'Med%', 'Hard%']
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
df = df.drop(columns=['#', 'Team', 'BABIP'])
df = df.sort_values('Name')
df.to_csv('BattedBalls', index=False)


# Scrape data for league average dashboard stats 2019
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=8&season=2019&month=0&season1=2019&ind=0&team=0,ss&rost=0&age=0&filter=&players=0'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['Name', 'Team', 'W', 'L', 'SV', 'G', 'GS', 'IP', 'K/9', 'BB/9',
           'HR/9', 'BABIP', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP', 'WAR']
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
df = df.drop(columns=['Name'])
df = df.sort_values('Team')
df.to_csv('LA-DashboardStats-2019', index=False)

# Scrape data for league average dashboard stats 2018
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=8&season=2018&month=0&season1=2018&ind=0&team=0,ss&rost=0&age=0&filter=&players=0'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['Name', 'Team', 'W', 'L', 'SV', 'G', 'GS', 'IP', 'K/9', 'BB/9',
           'HR/9', 'BABIP', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP', 'xFIP', 'WAR']
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
df = df.drop(columns=['Name'])
df = df.sort_values('Team')
df.to_csv('LA-DashboardStats-2018', index=False)


# Scrape league average advanced data 2019
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=1&season=2019&month=0&season1=2019&ind=0&team=0,ss&rost=0&age=0&filter=&players=0'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['#', 'Season', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP', 'LOB%', 'ERA-', 'FIP-', 'xFIP-', 'ERA', 'FIP', 'E-F', 'xFIP', 'SIERA']
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
df = df.drop(columns=['#', 'K/9', 'BB/9', 'HR/9', 'BABIP', 'LOB%', 'ERA', 'FIP', 'xFIP'])
df.to_csv('LA-AdvancedStats-2019', index=False)


# Scrape league average advanced data 2018
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=1&season=2018&month=0&season1=2018&ind=0&team=0,ss&rost=0&age=0&filter=&players=0'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['#', 'Season', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 'AVG', 'WHIP', 'BABIP', 'LOB%', 'ERA-', 'FIP-', 'xFIP-', 'ERA', 'FIP', 'E-F', 'xFIP', 'SIERA']
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
df = df.drop(columns=['#', 'K/9', 'BB/9', 'HR/9', 'BABIP', 'LOB%', 'ERA', 'FIP', 'xFIP'])
df.to_csv('LA-AdvancedStats-2018', index=False)


# Scrape League average BattedBalls data 2019
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=2&season=2019&month=0&season1=2019&ind=0&team=0,ss&rost=0&age=0&filter=&players=0'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['#', 'Season', 'BABIP', 'GB/FB', 'LD%', 'GB%', 'FB%', 'IFFB%', 'HR/FB', 'RS', 'RS/9', 'Balls', 'Strikes', 'Pitches', 'Pull%', 'Cent%', 'Oppo%', 'Soft%', 'Med%', 'Hard%']
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
df = df.drop(columns=['#'])
df.to_csv('LA-BattedBalls-2019', index=False)


# Scrape League average BattedBalls data 2018
URL = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=0&type=2&season=2018&month=0&season1=2018&ind=0&team=0,ss&rost=0&age=0&filter=&players=0'
print(URL)
# start scrape
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# Columns of chart to be scraped
columns = ['#', 'Season', 'BABIP', 'GB/FB', 'LD%', 'GB%', 'FB%', 'IFFB%', 'HR/FB', 'RS', 'RS/9', 'Balls', 'Strikes', 'Pitches', 'Pull%', 'Cent%', 'Oppo%', 'Soft%', 'Med%', 'Hard%']
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
df = df.drop(columns=['#'])
df.to_csv('LA-BattedBalls-2018', index=False)