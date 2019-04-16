from rStats import *
from pitcher_dictionary import *
from Standard_Deviation import *
from rStats import *
import copy


ogPitcherValue = pitcherDict['Aaron Nola']['ERA']
laValue19 = lasDict19['ERA']
laValue18 = lasDict18['ERA']
std = standardDeviationDict['ERA']

print(ogPitcherValue)
print(laValue19)
print(laValue18)
print(std)

val = float(ogPitcherValue) * laValue18
print(val)







# larpsDict[pitcher][cat] = ((pitcherDict[pitcher][cat] - ((lasDict[cat + '_19'] * lasDict[cat + '_18']) /2 )) / standardDeviationDict[cat])