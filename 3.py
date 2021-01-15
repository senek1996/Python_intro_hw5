# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:05:08 2021

@author: Lenovo
"""

pth='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\employees.txt'

summa=0
cou=0

with open(pth,'r',encoding='utf-8') as f:
    print('Сотрудники с ЗП менее 20000 р.:')
    for s in f:
        salary=float(s.split(' ')[1])
        summa+=salary
        cou+=1
        if salary<20000:
            print(s)
        
    
print('Средняя зарплата: {0:.2f} р.'.format(summa/cou))