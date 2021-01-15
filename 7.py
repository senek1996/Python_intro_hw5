# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:36:29 2021

@author: Lenovo
"""

import json
pth1='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\finance.txt'
pth2='C:\\Users\\Lenovo\\Documents\\Python Scripts\\GeekBrains\\Python_intro\\hw5_f\\finance.json'
i_want_use_a_Russian_text=True #True, если есть русские буквы в данных

firmas=[[],[]]
res_pol=0 #сумма прибылей
cou_pol=0 #количество фирм, отработавших в плюс

with open(pth1,'r',encoding='utf-8') as f:
    for s in f:
        s=s.split(' ')
        firmas[0].append(s[0])
        pr=float(s[2])-float(s[3])
        firmas[1].append(pr)
        if pr>=0:
            res_pol+=pr
            cou_pol+=1
    
for i in range(len(firmas[0])):
    print('Фирма {0} - {1} {2} р.'.format(firmas[0][i],'прибыль равна' if firmas[1][i]>=0 else 'убыток равен',abs(firmas[1][i])))
    
print('Средняя прибыль фирм, отработавших без потерь: {0:.2f} р.'.format(res_pol/cou_pol))

firmas_json=[{},{}]
res=0 #сумма результатов
cou=0 #количество всех фирм
for i in range(len(firmas[0])):
    firmas_json[0][firmas[0][i]]=firmas[1][i]
    res+=firmas[1][i]
    cou+=1
    
firmas_json[1]['avg_profit']=res/cou

if i_want_use_a_Russian_text:
    with open(pth2,'w',encoding='utf-8') as f:
        json.dump(firmas_json,f)
else:
    with open(pth2,'w') as f:
        json.dump(firmas_json,f)