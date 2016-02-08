# The Riddler - February 7, 2016
## Problem - How Many Cars Will Get Stuck In Traffic?
There is a very long, straight highway with some number of cars (N) placed somewhere along it, randomly.
The highway is only one lane, so the cars can’t pass each other. Each car is going in the same direction, and each
driver has a distinct positive speed at which she prefers to travel. Each preferred speed is chosen at random.
Each driver travels at her preferred speed unless she gets stuck behind a slower car, in which case she remains
stuck behind the slower car. On average, how many groups of cars will eventually form? (A group is one or more
cars travelling at the same speed.)For example, if the car in the very front happens to be slowest, there will be
exactly one group — everybody will eventually pile up behind the slowpoke. If the cars happen to end up in order,
fastest to slowest, there will be N groups — no car ever gets stuck behind a slower car.

## Solution
To solve this problem we will generate N cars each having a speed chosen at random from 0 to 1. When a Car, A, is generated
its speed is checked against the previously generated car A-1. If A.speed is > A-1.speed then the car will be added into the
same list as car A. If A.speed <= A-1.speed then the list containing car A-1 will be added to a list of lists and
car A will be placed in a new empty list. This process will be repeated until N cars have been generated. The number of
nested lists is then counted to determine the total number of groups or bunches of cars.

## Results
The simulation was run 100 times for N cars where N ranges from 1 to 100000 by 100. The result can be seen below where the
red area is +- 1 standard deviation.


# ![alt text](https://github.com/rd11490/The-Riddler-Traffic/blob/master/Feb_5_16/Results.png "Simulation Results")