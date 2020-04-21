#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:46:15 2020
@author: mgao
"""

import numpy as np

def annual_return(return_arr):
    '''
    传入一个收益率序列
    '''
    P0 = 1 # 假设初始值为1
    Pt = np.prod(return_arr + 1) # 计算卖出价值
    n = len(return_arr) # 计算投资期
    result = (Pt / P0) ** (250 / n) - 1 # 计算年化收益率
    return result

def annual_volatility(return_arr):
    '''
    传入一个收益率序列
    '''
    v_d = np.nanstd(return_arr)
    v_y = v_d * np.sqrt(250)
    return v_y
    
def maxdrawdown(price_arr):
    '''
    传入净值序列
    计算最大回撤
    '''
    i = np.argmax((np.maximum.accumulate(price_arr) - price_arr) / np.maximum.accumulate(price_arr)) # end of the period
    j = np.argmax(price_arr[:i]) # start of period
    mdd = (1 - price_arr[i] / price_arr[j])
    return mdd

def Sharp_Ratio(return_arr, risk_free_rate):
    '''
    传入收益率序列
    无风险收益率rf
    '''
    rf = risk_free_rate
    E = np.nanmean(return_arr)
    sigma = np.nanstd(return_arr)
    sharp_ratio = (E - rf) / sigma
    return sharp_ratio