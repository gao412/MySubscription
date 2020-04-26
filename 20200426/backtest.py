#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:18:30 2020

@author: mgao
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts
token = 'fa1d610c5755403e108bff96c6d6b660c4a004cb36affbb3e4da70c5'
ts.set_token(token)
pro = ts.pro_api()
import indicator


class TwoLines(object):
    def __init__(self, short, long, code, start, end):
        self.short = short
        self.long = long
        self.code = code
        self.start = start
        self.end = end
        self.net_value = 1
        self.pct_chg = 0
        try:
            print("数据获取中......")
            data = pro.daily(ts_code = self.code, start_date = self.start, end_date = self.end)
            data = data.iloc[::-1]
            data.reset_index(drop=True,inplace=True)
            self.close = data['close']
            print("数据获取成功")
        except:
            print("数据获取失败")

    def signal_adjust(self, s_buy, s_sell):
        a = np.where(s_buy == True)
        b = np.where(s_sell == True)
        a = a[0]
        b = b[0]
        
        if a[0] > b[0]:
            a = a
            b = b[1:]
            length = min(len(a), len(b))
            a = a[:length]
            b = b[:length]
        else:
            length = min(len(a), len(b))
            a = a[:length]
            b = b[:length]
        return a, b
    
    def create_signal(self):
        MA_short = self.close.rolling(self.short).mean()
        MA_long = self.close.rolling(self.long).mean()
        signal_buy = np.logical_and(MA_short.shift(1) < MA_long.shift(1), MA_short > MA_long)
        signal_sell = np.logical_and(MA_short.shift(1) > MA_long.shift(1), MA_short < MA_long)
        signal_buy, signal_sell = self.signal_adjust(signal_buy, signal_sell)
        return signal_buy, signal_sell
    
    def backtest(self):
        signal_buy, signal_sell = self.create_signal()
        result = np.zeros_like(self.close)
        pct_chg = self.close / self.close.shift(1) - 1
        for start, end in zip(signal_buy, signal_sell):
            result[start: end] = pct_chg[start: end]
        result = np.cumprod(result + 1)
        self.net_value = result
        temp = pd.DataFrame(result)
        self.pct_chg = temp / temp.shift(1) - 1
    
    def plot_net_value(self):
        result = self.net_value
        plt.plot(result)
        plt.ylabel('Net Value')
        plt.show()
        
        print('-'*30)
        print('最终的净值为{:.2f}'.format(result[-1]))
        print('-'*30)

    def evaluation(self):
        nv = self.net_value
        pct_chg = self.pct_chg
        result = pd.DataFrame()
        data = {'短线': self.short, '长线': self.long, \
                '最大回撤率': indicator.maxdrawdown(nv), \
                '夏普比率': indicator.Sharp_Ratio(pct_chg, 0)}
        result = result.append(data, ignore_index=True)
        print(result)
        return result
