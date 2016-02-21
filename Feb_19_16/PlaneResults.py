import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

frame = pd.read_csv('Extended_results.csv', index_col=0)
print(frame.columns)
avg_frame = pd.DataFrame()
upper_limit = pd.DataFrame()
lower_limit = pd.DataFrame()

for seat in frame['Num Passengers'].unique():
    seat_frame = frame[frame['Num Passengers'] == seat]
    average = seat_frame.mean()
    interval = 1.96*seat_frame.std()/np.sqrt(1000)
    lower = average-interval
    upper = average+interval
    avg_frame = avg_frame.append(average, ignore_index=True)
    upper_limit = upper_limit.append(upper, ignore_index=True)
    lower_limit = lower_limit.append(lower, ignore_index=True)

avg_frame = avg_frame.fillna(0)
upper_limit = upper_limit.fillna(0)
lower_limit = lower_limit.fillna(0)
"""
FCG -   08fb2a
FCB -   334d37
BCG -   bc3ee0
BCB -   bfc0c2
EPG -   b3cde8
EPP -   fbfb4f
EPB -   67f4f6
EPT -   1a3c68
EG  -   ffa200
EP  -   4f432d
EB  -   7d4f4f
ET  -   fb7a7a
"""
N = 12
ind = np.arange(N)*4
width = 1
colors = ['#08fb2a', '#334d37', '#bc3ee0', '#bfc0c2', '#b3cde8', '#b3cde8', '#fbfb4f', '#67f4f6', '#1a3c68', '#ffa200',
          '#4f432d', '#7d4f4f', '#fb7a7a']
labels = ["First Class\n Good", "First Class\n Bad", "Business \nClass Good", "Business \nClass Bad",
          "Econ Plus\n Good", "Econ Plus\n Middle", "Econ Plus\n Poor", "Econ Plus\n Bad",
          "Econ Good", "Econ Middle", "Econ Poor", "Econ Bad"]
for p in avg_frame["Num Passengers"]:
    plt.clf()
    avg_frame_pass = avg_frame[avg_frame['Num Passengers']==p]
    upper_frame_pass = upper_limit[upper_limit['Num Passengers']==p]
    vals1 = [avg_frame_pass.iloc[0]['FCG total'], avg_frame_pass.iloc[0]['FCB total'], avg_frame_pass.iloc[0]['BCG total'],
            avg_frame_pass.iloc[0]['BCB total'], avg_frame_pass.iloc[0]['EPG total'], avg_frame_pass.iloc[0]['EPP total'],
            avg_frame_pass.iloc[0]['EPB total'], avg_frame_pass.iloc[0]['EPT total'], avg_frame_pass.iloc[0]['EG total'],
            avg_frame_pass.iloc[0]['EP total'], avg_frame_pass.iloc[0]['EB total'], avg_frame_pass.iloc[0]['ET total']]

    vals2 = [upper_frame_pass.iloc[0]['FCG total'], upper_frame_pass.iloc[0]['FCB total'], upper_frame_pass.iloc[0]['BCG total'],
            upper_frame_pass.iloc[0]['BCB total'], upper_frame_pass.iloc[0]['EPG total'], upper_frame_pass.iloc[0]['EPP total'],
            upper_frame_pass.iloc[0]['EPB total'], upper_frame_pass.iloc[0]['EPT total'], upper_frame_pass.iloc[0]['EG total'],
            upper_frame_pass.iloc[0]['EP total'], upper_frame_pass.iloc[0]['EB total'], upper_frame_pass.iloc[0]['ET total']]
    plt.ylim(0, .5)
    plt.tick_params(axis='y', labelleft="off")
    plt.ylabel('% of section in incorrect seat')
    plt.title('Passengers in the Wrong Seat When Passenger: ' + str(p) + " Boards")
    plt.xticks(ind+width, labels, rotation='vertical')
    bar1 = plt.bar(ind, vals1, width, color=colors)
    bar2 = plt.bar(ind+2*width, vals2, width, color=colors)
    plt.tight_layout()

    for b in bar1:
        height = b.get_height()
        if height>0:
            plt.text(b.get_x()+.25, 1.05*height, '{:.2f}'.format(height)[2:], fontsize="xx-small")

    for b in bar2:
        height = b.get_height()
        if height>0:
            plt.text(b.get_x()+.25, 1.05*height, '{:.2f}'.format(height)[2:],fontsize="xx-small")

    plt.savefig("Totals/passsenger_"+str(p)+".png")

"""
fig2 = plt.figure()
plt.plot(avg_frame['FCG class'], color='#08fb2a')
plt.plot(avg_frame['FCB class'], color='#334d37')
plt.plot(avg_frame['BCG class'], color='#bc3ee0')
plt.plot(avg_frame['BCB class'], color='#bfc0c2')
plt.plot(avg_frame['EPG class'], color='#b3cde8')
plt.plot(avg_frame['EPP class'], color='#fbfb4f')
plt.plot(avg_frame['EPB class'], color='#67f4f6')
plt.plot(avg_frame['EPT class'], color='#1a3c68')
plt.plot(avg_frame['EG class'], color='#ffa200')
plt.plot(avg_frame['EP class'], color='#4f432d')
plt.plot(avg_frame['EB class'], color='#7d4f4f')
plt.plot(avg_frame['ET class'], color='#fb7a7a')
plt.title('Passengers in the Wrong Section')
plt.ylabel('% of section incorrect')
plt.xlabel('Passengers on the Plane')
plt.legend(loc='upper left')
plt.xlim(0, 400)
plt.ylim(0, 0.5)
plt.show()
"""