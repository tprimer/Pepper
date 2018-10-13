import Attacks
from importlib import reload as rl
import sys

class Test:

    def __init__(self,attBonusRange=range(5),defTargetRange=range(4,13),vantage=None):
        self.repetitions=10000
        self.attBonusRange=attBonusRange
        self.defTargetRange=defTargetRange
        self.vantage = vantage

        self.tests = {}
        for attBonus in attBonusRange:
            self.tests[attBonus]={}
            for defTarget in defTargetRange:
                attempts = [Attacks.Attempt(target=defTarget,maxBonus=attBonus,vantage=vantage) for x in range(self.repetitions)]
                successes = [attempt.outcome for attempt in attempts].count('success')
                failures = [attempt.outcome for attempt in attempts].count('failure')
                percent = successes/self.repetitions
                self.tests[attBonus][defTarget] = {'attempts':attempts,'successes':successes,'failures':failures,'percent':percent}

    def printResults(self):


        print('    ',' '.join(['  {:2d}\t'.format(defTarget) for defTarget in self.defTargetRange]))
        for attBonus in self.attBonusRange:
            #percentString = '\t'.join(['{:4.2f}%'.format(self.tests[attBonus][defTarget]['percent']*100.0 for defTarget in self.defTargetRange)])
            percentString = '\t'.join(['{:4.1f}%'.format(self.tests[attBonus][x]['percent'] * 100.0) for x in self.defTargetRange])

            print('{:}: '.format(attBonus),percentString)


class NewTest:

    def __init__(self, attBonusRange=range(5), defTargetRange=range(4,13), vantage=None):
        rl(Attacks)
        self.repetitions = 100
        self.attBonusRange = attBonusRange
        self.defTargetRange = defTargetRange
        self.vantage = vantage

        self.tests = {}
        count = 0
        for attBonus in attBonusRange:
            self.tests[attBonus] = {}
            for defTarget in defTargetRange:
                attempts = [Attacks.Attack(targetDefence=defTarget,attackBonus=attBonus,vantage=vantage) for x in range(self.repetitions)]
                successes = [attempt.hitResult for attempt in attempts].count(True)
                failures = [attempt.hitResult for attempt in attempts].count(False)
                percent = successes/self.repetitions
                self.tests[attBonus][defTarget] = {'attempts':attempts,'successes':successes,'failures':failures,'percent':percent}
                count = count + 1
                sys.stdout.write("Test progress: %d   \r" % (count))
                sys.stdout.flush()

    def printResults(self):


        print('    ',' '.join(['  {:2d}\t'.format(defTarget) for defTarget in self.defTargetRange]))
        for attBonus in self.attBonusRange:
            #percentString = '\t'.join(['{:4.2f}%'.format(self.tests[attBonus][defTarget]['percent']*100.0 for defTarget in self.defTargetRange)])
            percentString = '\t'.join(['{:4.1f}%'.format(self.tests[attBonus][x]['percent'] * 100.0) for x in self.defTargetRange])

            print('{:}: '.format(attBonus),percentString)

        datafile = open("attack_data.dat", 'w')
        for attBonus in self.attBonusRange:
            for defTarget in self.defTargetRange:
                test = self.tests[attBonus][defTarget]['attempts']
                for attack in test:
                    lineText = "{:},{:},{:},{:},{:},{:},{:}\n".format(attBonus,defTarget,attack.critRange,attack.hitTotal,attack.hitResult,attack.critResult,attack.hitDamage)
                    datafile.write(lineText)
        datafile.close()



