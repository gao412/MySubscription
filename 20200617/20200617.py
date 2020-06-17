# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:29:53 2020

@author: gao
"""

import numpy as np
import numpy_financial as npf

#%%
def cal_interets(principal, rate, n, interest_type='simple'):
    '''
    计算本息和
    ---------
    Params:
    ------
    principal: -> float 本金
    rate: -> float 利率
    n: -> float 年份
    interest_type: -> str 单利(simple)|复利(compound)|连续复利(continuous)
    
    Returns:
    -------
    future value : -> float 终值
    '''
    if interest_type == 'simple':
        final = principal * (1 + rate * n)
    elif interest_type == 'compound':
        final = principal * (1 + rate) ** n
    elif interest_type == 'continuous':
        final = principal * np.exp(rate * n)
    else:
        raise Exception('Invalid Type!')
    return final

#%%
# 计算终值
npf.fv(0.1, 4, 0, -1000)

# 计算现值
npf.pv(0.1, 4, 0, -1500)

# 计算净现值
rate, cashflows = 0.08, [-40_000, 5_000, 8_000, 12_000, 30_000]
npf.npv(rate, cashflows).round(5)

#%%
npf.pv(0.06, 3, -100, 0)
npf.pv(0.06, 3, -100, 0, when='begin')

# 验证
npf.pv(0.06, 3, 100, 0, when='begin') / npf.pv(0.06, 3, 100, 0) == 1.06

npf.fv(0.06, 3, -100, 0)
npf.fv(0.06, 3, -100, 0, when='begin')

# 验证
npf.fv(0.06, 3, 100, 0, when='begin') / npf.fv(0.06, 3, 100, 0) == 1.06

#%%
round(npf.irr([-100, 39, 59, 55, 20]), 5)
round(npf.irr([-100, 0, 0, 74]), 5)
round(npf.irr([-100, 100, 0, -7]), 5)
round(npf.irr([-100, 100, 0, 7]), 5)
round(npf.irr([-5, 10.5, 1, -8, 1]), 5)


