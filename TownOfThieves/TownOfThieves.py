
import random
import collections

class TownOfThieves:

    def __init__(self, townSize = 1000, startingCash = 100, maxYears = 1):
        self.households = townSize * [startingCash]
        self.year = 0
        self.maxYears = maxYears
        self.lottoOrder = self.lottery()
        self.targets = []

    def calculateStats(self):
        maximum = max(self.households)
        minimum = min(self.households)
        robbedPercent = float(len(set(self.targets))) / float(len(self.households))
        robbedMultiple = [item for item, count in collections.Counter(self.targets).items() if count > 1]
        lostAll = [target for target in set(self.targets) if self.households[target] == 0]

        robbedMultiplePercent = float(len(robbedMultiple))/float(len(self.households))
        lostAllPercent = float(len(lostAll)) / float(len(self.households))

        valueByLotto = [self.households[house] for house in self.lottoOrder]

        return (maximum, minimum, robbedPercent, robbedMultiplePercent, lostAllPercent, valueByLotto)

    def printStatus(self):
        print("Year: {0}".format(self.year))
        print("\n")
        print("Households")
        print(self.households)
        print("\n")

    def simulate(self):
        while self.year < self.maxYears:
            if (self.year > 0):
                self.households = [x + 100 for x in self.households]
            self.robHouses()
            self.year += 1

    def robHouses(self):
        #self.lottoOrder = self.lottery()
        for l in self.lottoOrder:
            self.robHouse(l)

    def lottery(self):
        households = list(range(0, len(self.households)-1))
        random.shuffle(households)
        return households

    # Pass in an index of the house that will do the robbing
    def robHouse(self, household):
        target = household
        while (target == household):
            target = random.randint(0, len(self.households)-1)
        self.targets.append(target)
        self.steal(household, target)

    # Pass in index of house doing robbing and house being robbed
    # transfer wealth from target to household
    def steal(self, household, target):
        self.households[household] += self.households[target]
        self.households[target] = 0