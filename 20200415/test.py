#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:39:27 2020

@author: mgao
"""

import tushare as ts
import numpy as np
import pandas as pd
import indicator
token = '设置你的token'
ts.set_token(token)
pro = ts.pro_api()

code = '002230.SZ'
startdate = '20190101'
enddate = '20190630'
data = pro.daily(ts_code=code, start_date=startdate, end_date=enddate)

data.head()

data = data.iloc[::-1]
data.reset_index(drop=True, inplace=True)
data.head()

ar = indicator.annual_return(data['pct_chg'].iloc[1:] / 100)
av = indicator.annual_volatility(data['pct_chg'] / 100)
maxdrawdown = indicator.maxdrawdown(data['close'])
sr = indicator.Sharp_Ratio(data['pct_chg'] / 100, 0)

print('年化收益率为{:.2f}'.format(ar))
print('年化波动率为{:.2f}'.format(av))
print('最大回撤率为{:.2f}'.format(maxdrawdown))
print('夏普比率为{:.2f}'.format(sr))
