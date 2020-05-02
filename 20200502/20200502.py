#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:31:52 2020

@author: mgao
"""

import pandas as pd
import matplotlib.pyplot as plt
from WindPy import *
w.start()

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

data = w.wsd("000001.SH,SPX.GI", "close", "2002-01-01", "2019-12-31", "")

sse = data.Data[0]
sp500 = data.Data[1]

date = data.Times

data = pd.DataFrame(index = date)
data['sse'] = sse
data['sp500'] = sp500

plt.plot(data['sse'], label = '上证指数')
plt.plot(data['sp500'], label = '标普500')
plt.title('指数走势图')
plt.legend()
plt.show()



