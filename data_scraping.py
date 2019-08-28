import csv
from player_ID_dict import *


def get_datascrape(month, day, year):
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
