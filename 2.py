# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 00:55:54 2021

@author: Lenovo
"""

class Clothes():
    
    def __init__(self,clo_prop,clo_prop_val):
        if  clo_prop.upper()=='V':
            self.name='Пальто'
        elif clo_prop.upper()=='H':
            self.name='Костюм'
        else:
            raise ValueError(f'Неверный параметр: {clo_prop}')
        
        self.val=clo_prop_val
    
    @property
    def calc_tkan(self):
        if self.name=='Пальто':
            cou_tkan=0.5+self.val/6.5        
            
        return('Для пошива этого '+self.name+' нужно '+str(cou_tkan)+' ткани')


#Только как. Не могу ума приложить, как использовать здесь абстрактные классы(
c1=Clothes('V',30)
print(c1.calc_tkan)