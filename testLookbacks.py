import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

msft = yf.Ticker("^DJI")

hist = msft.history(interval = '1m', start = '2020-05-12', end = '2020-05-19')

pts = []
for i in range(len(hist)):
    pts.append(hist.iloc[i]['Open'])


plt.plot(pts, 'r')


avgS = []
avgLastS = 34
for i in range(len(pts) - avgLastS):
    csum = 0
    for j in range(avgLastS):
        csum = csum + pts[i+j]
    avgS.append(csum/avgLastS)

avgL = []
avgLastL = 47
for i in range(len(pts) - avgLastL):
    csum = 0
    for j in range(avgLastL):
        csum = csum + pts[i+j]
    avgL.append(csum/avgLastL)

plt.plot(avgS, 'g')
plt.plot(avgL, 'b')


longPrevMore = avgL > avgL
buy = []
sell = []
actions = []

i = 0
less = min(len(avgL), len(avgS))
while( i < less):
    oldI = i
    while(i < less and avgL[i]<avgS[i]):
        i = i + 1
    if(i < less):
        sell.append(pts[i])
        actions.append(i)
        while(i < less and avgL[i]>avgS[i]):
            i = i + 1

        buy.append(pts[i])
        actions.append(i)
    if(i == oldI):
        break

diff = 0
buys = min(len(sell) , len(buy))
for i in range(buys):
    diff = diff + sell[i] - buy[i]

for i in range(len(actions)):
    plt.plot(actions[i], pts[i], 'ko')

print(diff)
plt.show()
