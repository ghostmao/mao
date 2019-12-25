# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:31:32 2019

@author: mwm
"""
import numpy as np
a1 =[[1,2,3],[4,5,6]] #列表
a2 = np.array(a1)   #列表 -----> 数组
a3 = np.mat(a1)      #列表 ----> 矩阵
a4 = a3.tolist()   #矩阵 ---> 列表
a5 = a2.tolist()   #数组 ---> 列表
a6 = np.mat(a2)   #数组 ---> 矩阵
a7 = np.array(a3)  #矩阵 ---> 数组

b1 =[1,2,3,4,5,6] #列表
b2=np.array(b1)   #列表 -----> 数组
b3 = np.mat(b1)      #列表 ----> 矩阵
b4 = b3.tolist()   #矩阵 ---> 列表
b5=b4[0]
b6=np.array(b3)
