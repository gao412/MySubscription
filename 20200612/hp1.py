#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 02:01:16 2020

@author: mgao
"""

import numpy as np
from numpy.linalg import inv
from numpy import dot

def hp_filter(x, lamb=1600):
    l = len(x)
    D = np.zeros((l, l))
    if l == 0:
        raise Exception("不能为空向量", l)
    else:
        if l == 1:
            D[0, 0] = 1
        elif l == 2:
            D[0, 0] = 1
            D[0, 1] = -2
            D[1, 0] = -2
            D[1, 1] = 5
        elif l == 3:
            D[0, :] = np.array([1, -2, 1])
            D[1, :] = np.array([-2, 5, -4])
            D[2, :] = np.array([1, -4, 6])
        elif l == 4:
            D[0, :] = np.array([1, -2, 1, 0])
            D[1, :] = np.array([-2, 5, -4, 1])
            D[2, :] = np.array([1, -4, 6, -4])
            D[3, :] = np.array([0, 1, -4, 6])
        elif l == 5:
            D[0, :] = np.array([1, -2, 1, 0, 0])
            D[1, :] = np.array([-2, 5, -4, 1, 0])
            D[2, :] = np.array([1, -4, 6, -4, 1])
            D[3, :] = np.array([0, 1, -4, 5, -2])
            D[4, :] = np.array([0, 0, 1, -2, 1])
        else:
            D[0, :3] = np.array([1, -2, 1])
            D[1, :4] = np.array([-2, 5, -4, 1])
            D[-1, -3:] = np.array([1, -2, 1])
            D[-2, -4:] = np.array([1, -4, 5, -2])
            for i in np.arange(2, l-2, 1):
                D[i, i-2:i+3] = np.array([1, -4, 6, -4, 1])
    g = dot(inv(lamb * D + np.eye(l)), x)
    return g
        