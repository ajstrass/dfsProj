import csv
standardDeviationDict = {}

catsList = ['IP', 'K/9' ,'BB/9' ,'HR/9' ,'BABIP' ,'LOB%' , 'GB%', 'HR/FB' ,'ERA' ,'FIP' ,
            'xFIP' ,'WAR' ,'K/BB' ,'K%' ,'BB%' ,'K-BB%' ,'AVG' ,'WHIP' ,'ERA-' ,'FIP-' ,'xFIP-'
    ,'E-F' ,'SIERA' ,'BABIP' ,'GB/FB' ,'LD%' ,'GB%' ,'FB%' ,'IFFB%' ,'HR/FB', 'RS', 'RS/9', 'Balls ',
            'Strikes' ,'Pitches' ,'Pull%' ,'Cent%' ,'Oppo%', 'Soft%' ,'Med%' ,'Hard%']

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
