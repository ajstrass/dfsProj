from bs4 import BeautifulSoup
import pandas as pd
import requests

import csv

# dictionary for storing player:ID
pidDict = {}

# stores all batters
batterList = []

# stores all ids
idList = []

with open('player-ids') as file:
    rowNum = 0
    reader = csv.reader(file)
    for row in reader:
        # skips first row
        if rowNum == 0:
            rowNum += 1
            # col by col adds batter to each list
            for pid in row:
                pidDict[pid] = 0
                batterList.append(pid)
        else:
            # col by col adds id to list
            for pid in row:
                idList.append(pid)

# combines 2 lists to Dictionary
pidDict = dict(zip(batterList, idList))