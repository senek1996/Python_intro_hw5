# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:58:35 2021

@author: Lenovo
"""

pth='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\data.txt'

cou_words=[]
cou_strs=0

with open(pth,'r') as f:
    for s in f:
        cou_words.append(len(s.split(' ')))
        cou_strs+=1

print('Характеристики файла: строк - {0}, слов по строкам - {1}'.format(cou_strs,cou_words))