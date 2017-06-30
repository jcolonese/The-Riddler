import pandas as pd
import TownOfThieves
import matplotlib.pyplot as plt
import numpy as np


def simulateOnce():
    town = TownOfThieves.TownOfThieves(1000, 100, 1)
    town.simulate()
    return town.calculateStats()


def valueOrZero(value):
    if value < 0:
        return 0.0
    else:
        return value


def simulate():
    pdStats = pd.DataFrame()
    pdValue = pd.DataFrame()
    for i in range(10000):
        print(i)
        out = simulateOnce()
        pdStats = pdStats.append(pd.Series([out[0], out[1], out[2], out[3], out[4]]), ignore_index=True)
        pdValue = pdValue.append(pd.Series(out[5]), ignore_index=True)

    pdStats.column = ["maximum", "minimum", "percentRobbed", "percentRobbedMoreThanOnce", "percentLeftWithNone"]
    print(pdStats.mean())
    matrix = pdValue.as_matrix()
    mean = np.mean(matrix, axis=0)
    std = np.std(matrix, axis=0)
    meanPlus = mean + std
    meanMinus = mean - std
    fixxer = lambda x: max(x, 0)
    vfunc = np.vectorize(fixxer)
    meanMinus = vfunc(meanMinus)
    plt.figure()
    plt.plot(mean, color='k', label="Average Value")
    plt.plot(meanPlus, color="r", label="Error")
    plt.plot(meanMinus, color="r")
    plt.legend(loc='upper left')
    plt.xlabel("Lottery Position")
    plt.ylabel("Cash Value at End of Day")
    plt.show()


simulate()
