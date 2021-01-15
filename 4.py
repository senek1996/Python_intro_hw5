# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:14:02 2021

@author: Lenovo
"""

pth1='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\numb1.txt'
pth2='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\numb2.txt'

names_numbers=[['One','Two','Three','Four'],['Один','Два','Три','Четыре']]
strs=[]

with open(pth1,'r') as f:
    for s in f:
        strs.append(s.split(' '))
    
for s in strs: #замена строк
    try:
        s[0]=names_numbers[1][names_numbers[0].index(s[0])]
    except:
        print('Перевода для числа {0} нет в словаре!'.format(s[0]))
    

with open(pth2,'w',encoding='utf-8') as f:
    for s in strs:
        f.write(' '.join(s))