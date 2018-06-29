import yaml
import random as rd
import numpy as np
from dice import roll


class character:
    def __init__(self, str=0, agi=0, att=0, dff=0):
        self.str = str
        self.agi = agi
        self.att = att
        self.dff = dff
        self.mainHand = None
        self.offHand = None

    def basic_attack(self, wep, target):
        dice = roll(2)
        total = sum(dice)+self.att
        if total >= target.dff+7:
            crit= 1 if dice[0]==dice[1] and dice[0]>=wep.critRange else 0
            damage = sum(roll(wep.hands))+wep.weight*self.str+wep.hands*crit
            return 1,crit,damage
        else:
            return 0,0,0

class weapon:
    def __init__(self, Name, Owner=None):
        self.Name = Name
        weap = yaml.safe_load(open("Weapons.yaml",'r'))[Name]
        self.size = weap['size']
        self.weight = weap['weight']
        self.hands = weap['hands']
        self.critRange = weap['critRange']
        if self.critRange == 'AGI':
                self.critRange = 6-Owner.agi


def test(weapon_Name):
    player = character(1, 2, 1, 1)
    mob = character(2, 1, 1, 0)
    player.mainHand = weapon(weapon_Name,Owner=player)
    hits = 0
    crits = 0
    damage = 0
    damage_hist = np.zeros(20)
    for i in range(10000):
        results = player.basic_attack(player.mainHand,mob)
        hits = hits+results[0]
        crits = crits+results[1]
        damage = damage+results[2]
        damage_hist[results[2]] = damage_hist[results[2]]+1

    print("Hits: ",hits)
    print("Crits: ",crits," (",crits/hits*100,"%)")
    print("Damage: ",damage)
    print("Average: ",damage/hits)
    print("Histogram: ",damage_hist)
    print("Weapon crit range: ",player.mainHand.critRange)

