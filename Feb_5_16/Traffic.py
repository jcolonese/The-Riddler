"""
There is a very long, straight highway with some number of cars (N) placed somewhere along it, randomly.
The highway is only one lane, so the cars can’t pass each other. Each car is going in the same direction, and each
driver has a distinct positive speed at which she prefers to travel. Each preferred speed is chosen at random.
Each driver travels at her preferred speed unless she gets stuck behind a slower car, in which case she remains
stuck behind the slower car. On average, how many groups of cars will eventually form? (A group is one or more
cars travelling at the same speed.)For example, if the car in the very front happens to be slowest, there will be
exactly one group — everybody will eventually pile up behind the slowpoke. If the cars happen to end up in order,
fastest to slowest, there will be N groups — no car ever gets stuck behind a slower car.

Extra credit: It’s time to offer up another 🏆 Coolest Riddler Extension Award 🏆. Spice up this mathematica
l roadtrip problem for your fellow readers. Alter the road, add a lane, enact some traffic laws, or something
far more creative than I can think of. Submit a description and analysis in the form below, or shoot me a link
to your work on Twitter. We’ll publish a winner next week.
"""
import random
import pandas as pd

class Car:
    def __init__(self):
        self.speed = random.random()


class Simulation:
    def __init__(self, N = 1000):
        self.N = N
        self.bunches = []
        self.car_count = 0
        self.last_speed = -1

        self.lengths = []
        self.speeds = []

    def runSim(self):
        cluster = []
        while self.car_count < self.N:
            c = self.add_car()
            if self.last_speed < 0:
                cluster.append(c)

            elif c.speed > self.last_speed:
                c.speed = self.last_speed
                cluster.append(c)

            elif c.speed <= self.last_speed:
                self.bunches.append(cluster)
                cluster = [c]

            self.last_speed = c.speed
        self.bunches.append(cluster)
        self.calc_results()
        #self.print_results()

    def add_car(self):
        self.car_count += 1
        return Car()

    def print_results(self):
        self.calc_results()
        print(len(self.lengths))
        for s in self.speeds:
            print(s)

    def calc_results(self):
        self.lengths = []
        self.speeds = []
        for b in self.bunches:
            self.lengths.append(len(b))
            for c in b:
                self.speeds.append(c.speed)

    def calc_avg_bunch(self):
        return sum(self.lengths)/len(self.lengths)


def main():
    frame = pd.DataFrame()
    for N in range(1, 100000, 100):
        print(N)
        for i in range(100):
            sim = Simulation(N)
            sim.runSim()
            frame = frame.append(pd.Series([N, len(sim.lengths), sim.calc_avg_bunch()]), ignore_index=True)
    frame.columns = ['Num Cars', 'Num Bunches', 'Avg Bunch Size']
    frame.to_csv('riddler_data.csv')
main()