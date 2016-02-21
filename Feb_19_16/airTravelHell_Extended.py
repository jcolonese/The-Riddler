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
import numpy as np

class Sim:
    def __init__(self, N = 374):
        self.N = N
        self.Plane_747 = Plane()
        self.tickets = list(range(1, self.N+1))
        self.ticket_adjusted = [x*x*x*x*x for x in self.tickets]
        self.ticket_weights = [x/sum(self.ticket_adjusted) for x in self.ticket_adjusted[::-1]]
        self.passengers = []

    def run_sim(self):
        self.create_passengers()
        p = self.passengers.pop()
        self.Plane_747.add_passenger_rand(p)
        while len(self.passengers) > 0:
            p = self.passengers.pop(0)
            self.Plane_747.add_passenger(p)

    def create_passengers(self):
        #while len(self.passengers) < self.N:
        seats = np.random.choice(self.tickets, p=self.ticket_weights, size=(len(self.tickets)), replace=False) - 1
        for seat in seats:
            ticket, ticket_class = self.tickets_from_seatnum(seat)
            self.passengers.append(Passenger(ticket, ticket_class))

    def tickets_from_seatnum(self, seat):
        if seat < 8:
            return seat, 'FCG'
        elif seat < 12:
            return seat-8, 'FCB'
        elif seat < 38:
            return seat-12, 'BCG'
        elif seat < 64:
            return seat-38, 'BCB'
        elif seat < 90:
            return seat-64, 'EPG'
        elif seat < 114:
            return seat-90, 'EPP'
        elif seat < 130:
            return seat-114, 'EPB'
        elif seat < 134:
            return seat-130, 'EPT'
        elif seat < 234:
            return seat-134, 'EG'
        elif seat < 332:
            return seat-234, 'EP'
        elif seat < 368:
            return seat-332, 'EB'
        else:
            return seat-368, 'ET'


"""
747-400 Dreamliner 374 seats
First Class - 12 seats - 8 good (FCG), 4 bad (FCB)
Business Class - 52 seats - 26 good (BCG), 26 bad (BCB)
Economy Plus - 70 seats - 26 good (EPG)- 24 poor (EPP)- 16 bad (EPB)- 4 terrible (EPT)
Economy - 240 seats - 100 good (EG)- 98 poor (EP)- 36 bad (EB)- 6 terrible(ET)
"""
class Plane:
    def __init__(self):
        self.N = 374
        self.num_passengers = 0
        self.seats = {'FCG': [None]*8, 'FCB': [None]*4, 'BCG': [None]*26, 'BCB': [None]*26, 'EPG': [None]*26,
                      'EPP': [None]*24, 'EPB': [None]*16, 'EPT': [None]*4, 'EG': [None]*100, 'EP': [None]*98,
                      'EB': [None]*36, 'ET': [None]*6}
        self.wrong_seats = pd.DataFrame()


    def add_passenger(self, p):
        if self.seats[p.ticket_class][p.ticket_seat] is None:
            p.seat = p.ticket_seat
            p.seat_class = p.ticket_class
            self.seats[p.ticket_class][p.ticket_seat] = p
        else:
            self.add_passenger_rand(p)
        self.num_passengers += 1
        self.wrong_seats = self.wrong_seats.append(pd.Series(self.get_wrong_seats()), ignore_index=True)

    def add_passenger_rand(self, p):
        for pref in p.preferences:
            inds = [i for i, x in enumerate(self.seats[pref]) if x is None]
            if len(inds) > 0:
                break
        p.seat_class = pref
        p.seat = random.choice(inds)
        self.seats[pref][p.seat] = p

    def get_wrong_seats(self):
        wrong_seat_list = [self.num_passengers]
        total_incorrect = 0
        for c in ['FCG', 'FCB', 'BCG', 'BCB', 'EPG', 'EPP', 'EPB', 'EPT', 'EG', 'EP', 'EB', 'ET']:
            incorrect_seat = 0
            incorrect_class = 0
            for s in self.seats[c]:
                if s is not None:
                    if s.seat_class != s.ticket_class:
                        incorrect_class += 1
                    elif s.seat != s.ticket_seat:
                        incorrect_seat += 1
            total_incorrect += incorrect_class + incorrect_seat
            wrong_seat_list.append(incorrect_class/len(self.seats[c]))
            wrong_seat_list.append((incorrect_seat+incorrect_class)/len(self.seats[c]))
        wrong_seat_list.append(total_incorrect)
        return wrong_seat_list


class Passenger:
    seat_preferences = [['FCG', 'FCB', 'BCG', 'BCB', 'EPG', 'EPP', 'EPB', 'EPT', 'EG', 'EP', 'EB', 'ET'], # First>business>econ+>econ
                        ['FCG', 'BCG', 'EPG', 'EG', 'EPP', 'EP', 'FCB', 'BCB', 'EPB', 'EB', 'EPT', 'ET']] #Good>poor>bad>terrible

    def __init__(self, ticket, ticket_class):
        self.ticket_seat = ticket
        self.ticket_class = ticket_class
        self.seat = None
        self.seat_class = None
        self.preferences = random.choice(self.seat_preferences)

Sim_Results_frame = pd.DataFrame()
for i in range(1000):
    print(i)
    s = Sim()
    s.run_sim()
    s.Plane_747.wrong_seats.columns = ['Num Passengers', 'FCG class', 'FCG total', 'FCB class', 'FCB total',
                                       'BCG class', 'BCG total', 'BCB class', 'BCB total', 'EPG class', 'EPG total',
                                       'EPP class', 'EPP total', 'EPB class', 'EPB total', 'EPT class', 'EPT total',
                                       'EG class', 'EG total', 'EP class', 'EP total', 'EB class', 'EB total',
                                       'ET class', 'ET total', 'Total Wrong']
    Sim_Results_frame = Sim_Results_frame.append(s.Plane_747.wrong_seats, ignore_index=True)
Sim_Results_frame.to_csv("Extended_results.csv")


"""
frame = pd.DataFrame()
for i in range(1000):
    s = Sim()
    s.run_sim()
    frame = frame.append(pd.Series(s.Plane_747.wrong_at_passenger), ignore_index=True)
plt.plot(list(frame.mean()), 'r')
plt.plot(list(frame.max()), 'k')
plt.plot(list(frame.min()), 'b')
plt.plot([a-b for a, b in zip(list(frame.mean()), list(frame.std()))], 'r')
plt.plot([a+b for a, b in zip(list(frame.mean()), list(frame.std()))], 'r')
plt.ylim(0, .1)
plt.show()
"""