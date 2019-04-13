from strasRating import *

leagueAverageStats = {}


for cat in cats:
    # ('stat value', 'std dev')
    leagueAverageStats[cat] = (0, 0)
row1 = []
row2 = []
with open('LA-DashboardStats-2018') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
       if count == 0:
           for col in row:
               row1.append(col)
               count = 1
       elif count == 1:
           for col in row:
               row2.append(col)


#print(row2)
#print(leagueAverageStats)