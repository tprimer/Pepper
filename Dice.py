import random as rd

class die:

    def __init__(self,sides=6):
        self.roll = rd.randint(1,sides)
        self.sides = sides

class diceRolls:

    def __init__(self,dice):
        self.dice = dice

    def __str__(self):
        return [die.roll for die in self.dice]

    def getRolls(self):
        rolls = [die.roll for die in self.dice]
        return rolls

    def replaceMin(self, die):
        self.getMinDie().roll = die.roll

    def replaceMax(self,die):
        self.getMaxDie().roll = die.roll

    def getMaxDie(self):
        rolls = self.getRolls()
        maxDie = self.dice[rolls.index(max(rolls))]
        return maxDieb

    def getMinDie(self):
        rolls = self.getRolls()
        minDie = self.dice[rolls.index(min(rolls))]
        return minDie

    def getSum(self):
        diceSum = sum([die.roll for die in self.dice])
        return diceSum

    def joinRolls(self,additionalRolls):
        joinedRolls = diceRolls(0)
        joinedRolls.dice = self.dice+additionalRolls.dice
        return joinedRolls

def roll(n, d=6, mod=None, drop=0):
    set = []
    for i in range(n):
        set.append(rd.randint(1, d))

    set.sort(reverse=True)

    return set