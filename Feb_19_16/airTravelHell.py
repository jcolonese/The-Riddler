"""
There’s an airplane with 100 seats, and there are 100 ticketed passengers each with an assigned seat. They line up to
board in some random order. However, the first person to board is the worst person alive, and just sits in a random
seat, without even looking at his boarding pass. Each subsequent passenger sits in his or her own assigned seat if it’s
empty, but sits in a random open seat if the assigned seat is occupied. What is the probability that you, the hundredth
passenger to board, finds your seat unoccupied?
"""

import random
import matplotlib.pyplot as plt
import pandas as pd

class Sim:
    def __init__(self, N):
        self.N = N
        self.Plane = Plane(self.N)
        self.tickets = list(range(self.N))
        self.passengers = []

    def run_sim(self):
        while len(self.passengers) < self.N:
            seat = random.choice(self.tickets)
            self.tickets.remove(seat)
            self.passengers.append(Passenger(seat))

        p = self.passengers.pop()
        self.Plane.add_passenger_rand(p)
        while len(self.passengers) > 0:
            p = self.passengers.pop()
            self.Plane.add_passenger(p)


class Plane:
    def __init__(self, N):
        self.N = N
        self.seats = [None]*N
        self.wrong_at_passenger = []

    def add_passenger(self, p):
        if self.seats[p.ticket] is None:
            p.seat = p.ticket
            self.seats[p.ticket] = p
        else:
            self.add_passenger_rand(p)
        self.wrong_at_passenger.append(self.get_wrong_seats())

    def add_passenger_rand(self, p):
        inds = [i for i, x in enumerate(self.seats) if x is None]
        p.seat = random.choice(inds)
        self.seats[p.seat] = p

    def get_wrong_seats(self):
        correct = 0
        incorrect = 0
        for s in self.seats:
            if s is not None:
                if s.seat == s.ticket:
                    correct += 1
                else:
                    incorrect += 1
        return incorrect/self.N


class Passenger:

    def __init__(self, seat):
        self.ticket = seat
        self.seat = None


frame = pd.DataFrame()
for i in range(1000):
    s = Sim(416) #416 seats on a standard 747
    s.run_sim()
    frame = frame.append(pd.Series(s.Plane.wrong_at_passenger), ignore_index=True)
plt.plot(list(frame.mean()), 'r')
plt.plot(list(frame.max()), 'k')
plt.plot(list(frame.min()), 'b')
plt.plot([a-b for a, b in zip(list(frame.mean()), list(frame.std()))], 'r')
plt.plot([a+b for a, b in zip(list(frame.mean()), list(frame.std()))], 'r')
plt.ylim(0, .1)
plt.show()