# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:25:47 2021

@author: Lenovo
"""

pth='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\timetable.txt'
disp=[]
disp_aggr={}

with open(pth,'r',encoding='utf-8') as f:
    for s in f:
        disp.append(s.split(' '))

for d in disp:
    sma=0 #сумма часов
    for i in range(1,len(d)):
        try:
            cou=float(d[i][0:d[i].index('(')])
        except:
            cou=0
        
        sma+=cou
        
    disp_aggr[d[0]]=sma

print(disp_aggr)