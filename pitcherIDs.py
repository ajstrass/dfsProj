import requests
import csv

# javascript:__doPostBack('LeaderBoard1$cmdCSV','')
data = requests.get('http://crunchtimebaseball.com/master.csv')
with open('playerIdCsv.csv', 'w') as f:
    writer = csv.writer(f)
    reader = csv.reader(data.text.splitlines())
    # reads file line by line
    rowNum = 0
    for row in reader:
        # writes file to lineup data
        writer.writerow(row)

playerIdsdict = {}

with open('playerIdCsv.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        for col in row:
            playerIdsdict[row[18]] = row[17]

playerIdsdict['Griffin Canning'] = '19867'


