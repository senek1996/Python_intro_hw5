# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:36:40 2021

@author: Lenovo
"""

pth='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\data.txt'

with open(pth,'w') as f:
    s=input('Введите строки. По окончании ввода введите пустую строку:')
    while s!='':
        f.write(s+'\n')
        s=input()
    
