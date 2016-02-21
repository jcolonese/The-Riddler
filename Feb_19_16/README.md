# The Riddler - February 19, 2016
## Problem - What's the chance there is someone sitting in your seat?
There’s an airplane with 100 seats, and there are 100 ticketed passengers each with an assigned seat. They line up to
board in some random order. However, the first person to board is the worst person alive, and just sits in a random
seat, without even looking at his boarding pass. Each subsequent passenger sits in his or her own assigned seat if it’s
empty, but sits in a random open seat if the assigned seat is occupied. What is the probability that you, the hundredth
passenger to board, finds your seat unoccupied?

## Solution - Extended Problem
To extend this problem we increase the number of seats on the plane from 100 to 374 and designate seats to separate
sections mimicking the layout of a Boeing 747-400.
The passengers board the plane in a weighted random order in which the person with the best ticket has a significantly
high chance of boarding next than the person with the worst ticket. If the passenger's seat is taken they will
randomly chose a new seat from the best available seats left (ex. If the passenger's seat is in First Class and it is
taken they will randomly chose a new seat in First Class, if First Class is full, they will move to the next section on
their preference list). Each passenger also has a preference list that dictates which section they will go to if their
section is full.
The two types of preferences are:
Section Based: First Class Good -> First Class Bad -> Business Class Good -> etc
or
Seat Quality Based: First Class Good -> Business Class Good  -> First Class Bad - > etc

![Plane Layout](https://github.com/rd11490/The-Riddler-Traffic/blob/master/Feb_19_16/Plane_Image.jpg)


## Results
The simulation was run 1000 times and the average number of people in the wrong seat in each section was plotted. In the
animation below the left bar represents the average number of passengers in the wrong seat and right bar represents the
upper bound of the 95% confidence interval.


![Results](https://github.com/rd11490/The-Riddler/blob/master/Feb_19_16/result.gif)