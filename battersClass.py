from battersDict import *

bcDict = {}

class Batter:
    def __init__(self, name, position, handedness):
        self.name = name
        self.position = position
        self.handedness = handedness


batterClassDict = {}

j = Batter('john', '1', 'right')


#batterClassDict = {Batter('name', '0', 'f') for batter in listOfBatters}



for batter in listOfBatters:
    batterClassDict[batter] = Batter(batter, '0', 'f')

# P = .083
# B = .079
#
# expMatchupKRate = (B * P) / (0.84 * B * P + 0.16)
#
# print(expMatchupKRate)