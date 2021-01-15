# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:09:41 2021

@author: Lenovo
"""

from random import randint

pth='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\numbs.txt'
numbs=20
sup=100 #верхняя граница

with open(pth,'w') as f:
    s=''
    for i in range(numbs):
        s+=(str(randint(0,sup))+' ')
    
    s=s[:len(s)-1] #убираем крайний пробел
    f.write(s)
    
summa=0
with open(pth,'r') as f:
    s=f.readline()
    nums=s.split(' ')
    for n in nums:
        summa+=int(n)
    

print('Сумма чисел из второго файла: {0}'.format(summa))