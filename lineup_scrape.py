import requests
import csv

# url of lineup webpage
data = requests.get('https://baseballmonster.com/Lineups.aspx?csv=1')
with open('lineupData.csv', 'w') as f:
    writer = csv.writer(f)
    reader = csv.reader(data.text.splitlines())
    # reads file line by line
    for row in reader:
        # writes file to lineup data
        writer.writerow(row)
