#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:47:36 2020

@author: mgao
"""

from backtest import TwoLines
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

short = 5
long = 10
code = '002230.SZ'
start = '20190101'
end = '20191231'


tl = TwoLines(short, long, code, start, end)

tl.backtest()
tl.plot_net_value()

tl.evaluation()

result = pd.DataFrame()

for i in np.arange(5, 20):
    for j in np.arange(20, 40):
        tl = TwoLines(i, j, code, start, end)
        tl.backtest()
        temp = tl.evaluation()
        result = pd.concat([result, temp])

result.reset_index(drop=True, inplace=True)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xpos = result['短线'].tolist()
ypos = result['长线'].tolist()
zpos = np.zeros(len(result)).tolist()

dx = np.ones(len(result))
dy = np.ones(len(result))
dz = result['夏普比率']
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color = '#00ceaa')
plt.show()

result.sort_values(by='夏普比率', ascending=False)

result.sort_values(by='最大回撤率', ascending=True)






