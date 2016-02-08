import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return a * np.log(x)+c


frame = pd.read_csv('riddler_data.csv', index_col=0)
avg_frame = pd.DataFrame()
for N in frame['Num Cars'].unique():
    single_frame = frame[frame['Num Cars'] == N]
    avg_frame = avg_frame.append(pd.Series([N, single_frame['Num Bunches'].mean(),
                single_frame['Num Bunches'].mean() - single_frame['Num Bunches'].std(),
                single_frame['Num Bunches'].mean() + single_frame['Num Bunches'].std()]),
                ignore_index=True)

popt_avg, pcov_avg = curve_fit(func, avg_frame[0], avg_frame[1])
popt_upper, pcov_upper = curve_fit(func, avg_frame[0], avg_frame[2])
popt_lower, pcov_lower = curve_fit(func,avg_frame[0], avg_frame[3])

plt.plot(avg_frame[0], avg_frame[1], 'xb', label='Mean')
#plt.plot(avg_frame[0], avg_frame[2], 'or')
#plt.plot(avg_frame[0], avg_frame[3], 'or')
plt.plot(avg_frame[0], func(avg_frame[0], *popt_avg), 'k', label='Line of Best Fit')
plt.fill_between(avg_frame[0], func(avg_frame[0], *popt_upper), func(avg_frame[0], *popt_lower), facecolor='red', alpha =0.5, label='$\pm 1 Standard Deviation')
#plt.plot(avg_frame[0], func(avg_frame[0], *popt_lower), 'k')

plt.title('Number of Bunches per Number of Cars on the Road')
plt.ylabel('Number of Bunches')
plt.xlabel('Number of Cars')
plt.legend(loc='upper left')
plt.xlim(0, 100000)
plt.ylim(0, 20)
plt.show()