import requests
import csv

# javascript:__doPostBack('LeaderBoard1$cmdCSV','')

def set_pitcherIDS():
    data = requests.get('http://crunchtimebaseball.com/master.csv')
    with open('playerIdCsv.csv', 'w') as f:
        writer = csv.writer(f)
        reader = csv.reader(data.text.splitlines())
        # reads file line by line
        rowNum = 0
        for row in reader:
            # writes file to lineup data
            writer.writerow(row)

    pitcherIdsdict = {}

    with open('playerIdCsv.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            for col in row:
                pitcherIdsdict[row[18]] = row[17]

    pitcherIdsdict['Griffin Canning'] = '19867'
    print(pitcherIdsdict)