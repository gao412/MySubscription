# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:36:30 2020

@author: gao
"""

import pandas as pd
from datetime import datetime
from WindPy import *
w.start()

#%%
def Download_data_edb(fields,name,time1, time2,option):
    data = w.edb(fields, time1, time2, options=option)
    df = pd.DataFrame(data.Data,index=[name],columns=data.Times)
    return(df)

def Download_data_wss(codelist, namelist, date, fieldslist, fieldsnamelist, option):  # fields输入指标，option输入指标参数 ，wind w.wsd函数
    df = pd.DataFrame(columns=fieldsnamelist, index=namelist, dtype='float64')
    data = w.wss(codelist, fieldslist,  "tradeDate=" + date + ";"  + option).Data
    for i in range(len(fieldslist)):
        df.iloc[:, i] = data[i]
    return(df)

def Download_data_wsd(codelist,namelist,fields,time1, time2,option):  # fields输入指标，option输入指标参数 ，wind w.wsd函数
    data = w.wsd(codelist, fields, time1, time2, options=option)
    df = pd.DataFrame(data.Data,index=namelist,columns=data.Times)
    return(df)

#%%
data = w.edb('M5567876', '2019-01-01', '2019-12-31', '')
df = pd.DataFrame()
df['GDP'] = data.Data[0]
df.index = data.Times
df

data = w.wsd('002230.SZ', 'close', '2019-01-01', '2019-12-31', '')
df = pd.DataFrame()
df['收盘价'] = data.Data[0]
df.index = data.Times
df

data = w.wss("002230.SZ,601398.SH", "close,volume", "tradeDate=20200417;priceAdj=U;cycle=D")
df = pd.DataFrame()
df['收盘价'] = data.Data[0]
df['成交量'] = data.Data[1]
df.index = ['科大讯飞', '工商银行']
df







