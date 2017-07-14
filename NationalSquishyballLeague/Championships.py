from scipy.special import comb
import math
import pandas as pd
import matplotlib.pyplot as plt

prize = 1000000
discount = 10000
seriesLength = range(1, 100, 2)
winProb = .6

frame = pd.DataFrame()

for length in seriesLength:
    ## (n choose k)p^k(1-p)^n-k
    k = math.ceil(length / 2.0)
    seriesProb = 0.0
    for g in range(k, length + 1):
        combs = comb(g - 1, k - 1)
        prob = combs * (math.pow(winProb, k)) * math.pow(1 - winProb, g - k)
        # print("{} Wins In {} Games - Prob: {}".format(k, g, prob))
        seriesProb += prob
    money = prize - length * discount
    expectedValue = money * seriesProb
    frame = frame.append(pd.Series([length, k, money, seriesProb, expectedValue]), ignore_index=True)

frame.columns = ["SeriesLength", "Wins", "PossibleMoney", "WinPercent", "ExpectedValue"]

print(frame)

frame.to_csv("results.csv")

plotFrame = frame[["SeriesLength", "ExpectedValue"]]
arr = plotFrame.as_matrix()
plt.plot(arr[:, 0], arr[:, 1])
plt.xlabel("Series Length")
plt.ylabel("Expected Value")
plt.show()
