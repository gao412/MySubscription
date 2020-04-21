#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:26:25 2020

@author: mgao
"""

import numpy as np
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
import indicator
token = '设置你的token'
ts.set_token(token)
pro = ts.pro_api()


code = '002230.SZ'
startdate = '20180101'
enddate = '20191231'
data = pro.daily(ts_code=code, start_date=startdate, end_date=enddate)
data = data.iloc[::-1]
data.reset_index(drop=True,inplace=True)
data.head()


close = data['close']
plt.plot(close)
plt.ylabel('Price')
plt.show()



MA5 = close.rolling(5).mean()
MA20 = close.rolling(20).mean()
MA5.head(30)
MA20.head(30)
plt.plot(MA5, label='MA5')
plt.plot(MA20, label='MA20')
plt.legend()
plt.show()



signal_buy = np.logical_and(MA5.shift(1) < MA20.shift(1), MA5 > MA20)
signal_sell = np.logical_and(MA5.shift(1) > MA20.shift(1), MA5 < MA20)
np.where(signal_buy == True)
np.where(signal_sell == True)


def signal_adjust(s_buy, s_sell):
    a = np.where(s_buy == True)
    b = np.where(s_sell == True)
    if a[0][0] < b[0][0]:
        if len(a[0]) > len(b[0]):
            a = a[0][:-1]
        b = b[0]
    else:
        b = b[0][1:]
    return a, b

signal_buy, signal_sell = signal_adjust(signal_buy, signal_sell)


result = np.zeros_like(close)
pct_chg = close / close.shift(1) - 1

for start, end in zip(signal_buy, signal_sell):
    result[start: end] = pct_chg[start: end]

result = np.cumprod(result + 1)

plt.plot(result)
plt.ylabel('Net Value')
plt.show()

print('-'*30)
print('最终的净值为{:.2f}'.format(result[-1]))
print('-'*30)

nv = pd.DataFrame(result)
nv_chg = nv / nv.shift(1) - 1

ar = indicator.annual_return(nv_chg.iloc[1:].values.ravel())
av = indicator.annual_volatility(nv_chg.values.ravel())
maxdrawdown = indicator.maxdrawdown(nv.values.ravel())
sr = indicator.Sharp_Ratio(nv_chg.values.ravel(), 0)

print('年化收益率为{:.2f}'.format(ar))
print('年化波动率为{:.2f}'.format(av))
print('最大回撤率为{:.2f}'.format(maxdrawdown))
print('夏普比率为{:.2f}'.format(sr))






