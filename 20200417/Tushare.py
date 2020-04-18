# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:36:23 2020

@author: gao
"""

import tushare as ts
token = '设置你的token'
ts.set_token(token)
pro = ts.pro_api()

# 获取单只股票数据
df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
df

# 获取多只股票数据
df = pro.daily(ts_code='000001.SZ,600000.SH', start_date='20180701', end_date='20180718')
df
df.groupby('ts_code').max()

# 获取某日全部股票的指标
df = pro.daily_basic(ts_code='', trade_date='20180726', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
df

# 获取利润表数据
df = pro.income(ts_code='600000.SH', start_date='20180101', end_date='20180730', fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')
df


