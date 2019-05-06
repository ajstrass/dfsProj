from zScore_Pitcher import *
SSDict = {}
ZZDict = {}

pitcherVals = {}
for pitcher in pitcherList:
    kPerc = float(pitcherDict[pitcher]['K%']) * 12
    BBperc = float(pitcherDict[pitcher]['BB%']) * 12
    BABIP = float(pitcherDict[pitcher]['BABIP']) * 50
    GBR = pitcherDict[pitcher]['GB%']
    GBR = GBR.rstrip("%")
    GBR = float(GBR)
    GBR = (GBR/100) * 50
    FBR = pitcherDict[pitcher]['FB%']
    FBR = FBR.rstrip('%')
    FBR = float(FBR)
    FBR = (FBR / 100) * 50
    whip = float(pitcherDict[pitcher]['WHIP']) * 12
    siera = float(pitcherDict[pitcher]['SIERA']) * 2.5
    HCR = pitcherDict[pitcher]['Hard%']
    HCR = HCR.rstrip('%')
    HCR = float(HCR)
    HCR = (HCR / 100) * 50
    SCR = pitcherDict[pitcher]['Soft%']
    SCR = SCR.rstrip('%')
    SCR = float(SCR)
    SCR = (SCR / 100) * 50
    ssr = float(kPerc) - BBperc + BABIP + GBR - FBR - whip - siera - HCR + SCR
    SSDict[pitcher] = ssr

pitcherZVals = {}
for pitcher in pitcherList:
    kPer9 = float(zScorePitcherDict[pitcher]['K/9'])
    BBper9 = float(zScorePitcherDict[pitcher]['BB/9'])
    BABIP = float(zScorePitcherDict[pitcher]['BABIP'])
    GBR = pitcherDict[pitcher]['GB%']
    GBR = float(GBR)
    GBR = (GBR/100)
    FBR = zScorePitcherDict[pitcher]['FB%']
    FBR = float(FBR)
    FBR = (FBR / 100)
    whip = float(zScorePitcherDict[pitcher]['WHIP'])
    siera = float(zScorePitcherDict[pitcher]['SIERA'])
    HCR = zScorePitcherDict[pitcher]['Hard%']
    HCR = float(HCR)
    HCR = (HCR / 100)
    SCR = zScorePitcherDict[pitcher]['Soft%']
    SCR = float(SCR)
    SCR = (SCR / 100)
    ssr = float(kPer9) - BBper9 + BABIP + GBR - FBR - whip - siera - HCR + SCR
    ZZDict[pitcher] = ssr

orderedPitcherRanks = []
for x in pitcherList:
    orderedPitcherRanks.append((ZZDict[x], x))
    orderedPitcherRanks.sort()

print(orderedPitcherRanks)