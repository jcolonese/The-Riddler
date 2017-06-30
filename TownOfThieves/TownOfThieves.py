# coding=utf-8
"""
From Max Weinreich, a purge puzzle:

A town of 1,000 households has a strange law intended to prevent wealth-hoarding. On January 1 of every year,
each household robs one other household, selected at random, moving all of that house’s money into their own house.
The order in which the robberies take place is also random and is determined by a lottery.
(Note that if House A robs House B first, and then C robs A, the houses of A and B would each be empty and
C would have acquired the resources of both A and B.)

Two questions about this fateful day:

What is the probability that a house is not robbed over the course of the day?
Suppose that every house has the same amount of cash to begin with — say $100.
Which position in the lottery has the most expected cash at the end of the day, and what is that amount?
"""
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
            self.robHouses()
            #self.printStatus()
            self.year += 1

    def robHouses(self):
        self.lottoOrder = self.lottery()
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