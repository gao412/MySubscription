#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 03:31:56 2020

@author: mgao
"""

import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
dta = sm.datasets.macrodata.load_pandas().data
index = pd.date_range(start='1959Q1', end='2009Q4', freq='Q')
dta = dta.set_index(index)

cycle, trend = sm.tsa.filters.hpfilter(dta.loc[:, 'realgdp'], 1600)
gdp_decomp = dta[['realgdp']]
gdp_decomp.loc[:, "cycle"] = cycle
gdp_decomp.loc[:, "trend"] = trend

fig, ax = plt.subplots()
gdp_decomp.loc[:, ["realgdp", "trend"]].loc["2000-03-31":].plot(ax=ax,
                                                     fontsize=16)
plt.show()