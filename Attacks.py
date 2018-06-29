import Dice
import yaml
strength=2
critDamage=6

class Attack:

    def __init__(self,targetDefence=7,attackBonus=0,vantage=None,weapon=yaml.safe_load(open("Weapons.yaml",'r'))["Longsword"]):
        self.critRange = weapon.critRange
        self.baseRoll = Dice.diceRolls([Dice.die() for die in range(2)])
        self.bonusRoll = Dice.diceRolls([Dice.die() for die in range(attackBonus)])
        # self.hitResult = self.checkForHit(self.baseRoll,targetDefence)
        self.hitResult = self.checkForHit(self.baseRoll.joinRolls(self.bonusRoll), targetDefence)
        self.hitTotal  = self.getHitTotal(self.baseRoll.joinRolls(self.bonusRoll))
        self.critResult = self.checkForCrit(self.baseRoll,self.critRange)
        self.hitDamage = Dice.die().roll*weapon.hands+strength*weapon.weight+int(self.critResult)*weapon.hands if self.hitResult else 0.0

    def checkForCrit(self,baseRoll,critRange):
        return baseRoll.getRolls()[0]==baseRoll.getRolls()[1] and baseRoll.getRolls()[0]>=critRange

    def checkForHit(self,diceRolls,targetDefence):
        return sum(sorted(diceRolls.getRolls())[0:2])>=targetDefence

    def getHitTotal(self,diceRolls):
        return sum(sorted(diceRolls.getRolls())[0:2])

    def printResults(self):
        hitOrMiss = "Hit!" if self.hitResult else "Miss"
        critOrNot = "Crit! " if self.critResult else "Normal"
        print(critOrNot+" "+hitOrMiss+" "+
              " ".join(str(roll) for roll in self.baseRoll.getRolls())+
              " ".join(str(roll) for roll in self.bonusRoll.getRolls())+
              " = {:}".format(self.hitTotal)+
              " for {:} total damage".format(self.hitDamage)
              )