import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

msft = yf.Ticker("^DJI")

hist = msft.history(period = '5d', interval = '1m')

pts = []
for i in range(len(hist)):
    pts.append(hist.iloc[i]['Open'])


plt.plot(pts, 'r')

data = []
LLR = 40
SSR = 30
for LL in range(LLR):
    print(int(100*LL/LLR), "%")
    for SS in range(SSR):
        avgS = []
        avgLastS = 5 + SS
        for i in range(len(pts) - avgLastS):
            csum = 0
            for j in range(avgLastS):
                csum = csum + pts[i+j]
            avgS.append(csum/avgLastS)

        avgL = []
        avgLastL = 30 + LL
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
        data.append([avgLastS, avgLastL, diff])
iMax = 0
diffMax = -99999
for d in range(len(data)):
    if(data[d][2] > diffMax):
        diffMax = data[d][2]
        iMax =  d


print(data[iMax][0],data[iMax][1],100*data[iMax][2]/pts[0])