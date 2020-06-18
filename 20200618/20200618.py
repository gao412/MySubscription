# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:37:12 2020

@author: gao
"""

import numpy_financial as npf
import pandas as pd
import numpy as np

#%%
def bond_pricing(rate, r, n, M, m):
    '''
    债券定价
    -------
    Params
    rate: -> float 贴现率
    r: -> float 年利息率
    n: -> flaot 期限
    M: -> float 票面金额
    m: -> int 每年付息次数
    
    Return
    price: -> float 债券价格
    '''
    global cash_flow
    # 计算贴现率
    rate = rate / m
    # 计算每期利息率
    r = r / m
    # 计算每期利息
    C = M * r
    # 计算期数
    n = n * m
    # 汇总现金流到一个list中
    cash_flow = [0] + [C] * n
    price = npf.npv(rate, cash_flow) + M / (1 + rate) ** n
    return price
    
#%%
bond_pricing(0.12, 0.1, 10, 10000, 2)
# 8853.00787814347

#%%
def bond_pricing(rate, n, M, m):
    '''
    零息债券定价
    -------
    Params
    rate: -> float 贴现率
    n: -> flaot 期限
    M: -> float 票面金额
    m: -> int 每年付息次数
    
    Return
    price: -> float 债券价格
    '''
    # 计算贴现率
    rate = rate / m
    # 计算期数
    n = n * m
    price = npf.pv(rate, n, 0, -M)
    return price
#%%
bond_pricing(0.1, 15, 2000, 1)
# 478.7840987383267

#%%
def FRNs_pricing(rpc, rpnow, I0, Inow, f, m, d, n, P=100):
    '''
    浮动利率债券定价
    --------------
    Params
    P: -> float 票面金额 默认100
    rpc: -> float 固定风险贴水
    rpnow: -> float 当前风险贴水
    f: -> int 当日至下一个付息日的天数
    d: -> int 前后两个利率重设日的天数
    m: -> int 计息的次数
    n: -> int 下一个付息日起算至到期日的期数
    '''
    rbar = Inow + rpnow
    P_next = (((rpc - rpnow) * P / m) / ((1+rbar/m) ** np.arange(1, n+1))).sum()
    a = rpc + I0
    b = rpnow + Inow
    c = P + ((a - b) * P / m + P_next) / (1 + rbar * f / d)
    return c

#%%
FRNs_pricing(0.3/100, 0.25/100, 0.05, 4.5/100, 51, 4, 91, 8, 100)
# 100.22633579982538

#%%
def Macaulay_Duration(M, r, rate, n, m):
    '''
    计算麦考利久期
    -------------
    Params
    M: -> float 票面金额
    r: -> float 贴现率
    rate: -> float 票面利率
    n: -> int 年份
    m: -> int 每年计息次数    
    
    Returns
    -------
    D1: -> float 麦考利久期(以期数计)
    D2: -> float 麦考利久期(以年计)
    '''
    rate = rate / m
    r = r / m
    n = n * m
    C = rate * M
    PV = -npf.pv(r, n, C, M)
    
    df = pd.DataFrame(columns = ['期数','现金流','贴现值','占价格比率','与期数乘积'])
    df.loc[:, '期数'] = np.arange(1, n + 1)
    df.loc[:, '现金流'] = np.array([C] * (n-1) + [M+C])
    df.loc[:, '贴现值'] = df.loc[:, '现金流'].values / ((1 + r) ** df.loc[:, '期数'].values)
    df.loc[:, '占价格比率'] = df.loc[:, '贴现值'] / PV
    df.loc[:, '与期数乘积'] = df.loc[:, '期数'].values * df.loc[:, '占价格比率']
    D1 = df.loc[:, '与期数乘积'].sum()
    D2 = D1 / m
    return D1, D2

#%%
D1, D2 = Macaulay_Duration(1000, 0.1, 0.12, 3, 2)
print('按期计麦考利久期为{:.2f}'.format(D1))
print('按年计麦考利久期为{:.2f}'.format(D2))

























