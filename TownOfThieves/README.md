# The Riddler - June 30, 2017
## Problem - How much money will you have left?
From Max Weinreich, a purge puzzle:

A town of 1,000 households has a strange law intended to prevent wealth-hoarding. On January 1 of every year,
each household robs one other household, selected at random, moving all of that house’s money into their own house.
The order in which the robberies take place is also random and is determined by a lottery.
(Note that if House A robs House B first, and then C robs A, the houses of A and B would each be empty and
C would have acquired the resources of both A and B.)

Two questions about this fateful day:

1. What is the probability that a house is not robbed over the course of the day?

2. Suppose that every house has the same amount of cash to begin with — say $100.
Which position in the lottery has the most expected cash at the end of the day, and what is that amount?

## Solution
1. 36.8%

2. See Results below

## Results
The simulation was run 10000 times for 1000 households each starting with 100$. The expected ammount of money left at
the end of the day can be seen below where the red lines are +- 1 standard deviation.


# ![alt text](https://github.com/rd11490/The-Riddler/blob/master/TownOfThieves/figure_1.png "Simulation Results")