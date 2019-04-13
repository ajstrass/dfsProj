from pitcher_dictionary import *
#print(pitcherList)
SSDict = {}

x = float('1')
y = float('49')

z = x + y
print(z)


pitcherVals = {}
for pitcher in pitcherList:
    kPer9 = float(pitcherDict[pitcher]['K/9']) * 12
    BBper9 = float(pitcherDict[pitcher]['BB/9']) * 12
    BABIP = float(pitcherDict[pitcher]['BABIP']) * 50
    GBR = pitcherDict[pitcher]['GB%']
    GBR = GBR.rstrip("%")
    GBR = float(GBR)
    GBR = (GBR/100) * 50
    FBR = pitcherDict[pitcher]['FB%']
    FBR = float(FBR)
    FBR = (FBR / 100) * 50
    xFIP = float(pitcherDict[pitcher]['xFIP-']) * 2.5
    whip = float(pitcherDict[pitcher]['WHIP']) * 12
    siera = pitcherDict[pitcher]['SIERA'] * 2.5+
    HCR = pitcherDict[pitcher]['Hard%']
    HCR = float(HCR)
    HCR = (HCR / 100) * 50
    SCR = pitcherDict[pitcher]['Soft%']
    SCR = float(SCR)
    SCR = (SCR / 100) * 50
    ssr = float(kPer9) - BBper9 + BABIP + GBR - FBR - xFIP - whip - siera - HCR + SCR
    SSDict[pitcher] = ssr

orderedList = []
for x in pitcherList:
    orderedList.append((SSDict[x], x))
    orderedList.sort()
print(orderedList)
