#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:38:44 2020

@author: mgao
"""

# 大数定律
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(666)

data = np.random.rand(100000)
sns.distplot(data)

sample_size = []
sample_mean = []

for i in range(100, 100000, 100):
    sample_size.append(i)
    sample_mean.append(np.random.choice(data, i).mean())

result = pd.DataFrame({'Sample Size': sample_size, 'Sample Mean': sample_mean})

result.set_index('Sample Size', inplace=True)

result.plot()

plt.axhline(data.mean(), color = 'red')


# 中心极限定理
plt.figure(figsize = (9, 9))

plt.subplot(221)
sample_mean = []
for i in range(1,1000):
    s = np.random.choice(data,size = 500).mean()
    sample_mean.append(s)
sns.distplot(sample_mean)
plt.title("size = 500")

plt.subplot(222)
sample_mean = []
for i in range(1,1000):
    s = np.random.choice(data,size = 2000).mean()
    sample_mean.append(s)
sns.distplot(sample_mean)
plt.title("size = 2000")

plt.subplot(223)
sample_mean = []
for i in range(1,1000):
    s = np.random.choice(data,size = 5000).mean()
    sample_mean.append(s)
sns.distplot(sample_mean)
plt.title("size = 5000")

plt.subplot(224)
sample_mean = []
for i in range(1,1000):
    s = np.random.choice(data,size = 10000).mean()
    sample_mean.append(s)
sns.distplot(sample_mean)
plt.title("size = 10000")







