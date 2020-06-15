# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:49:59 2020

@author: mgao
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
from WindPy import *
w.start()

codelist = ['M5567889', 'M0039354']
namelist = ['GDP:当季值', 'GDP:当季同比']

df = pd.DataFrame(columns = namelist)
for i in range(len(namelist)):
    code = codelist[i]
    name = namelist[i]
    tmp = w.edb(code, '2010-01-01', '2019-12-31', '')
    df.loc[:, name] = tmp.Data[0]
    df.index = tmp.Times

plt.plot(df)
plt.legend(list(df.columns))
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
lns1 = ax.plot(df.iloc[:, 0], '-', label = df.columns[0])
ax2 = ax.twinx()
lns2 = ax2.plot(df.iloc[:, 1], '-r', label = df.columns[1])
# 将label合并起来
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.grid()
ax.set_xlabel("年")
ax.set_ylabel(r"亿元")
ax2.set_ylabel(r"%")
plt.show()
