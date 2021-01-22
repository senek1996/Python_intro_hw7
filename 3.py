# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 01:11:03 2021

@author: Lenovo
"""

class Cell():
    
    def __init__(self,cou_cells):
        self.count=cou_cells
    
    def __add__(self,b):
        return(Cell(self.count+b.count))
    
    def __sub__(self,b):
        if self.count-b.count>0:
            return(Cell(self.count-b.count))
        else:
            print('ПРЕДУПРЕЖДЕНИЕ: Количество ячеек в вычитаемой клетке должно быть МЕНЬШЕ')
            return
    
    def __mul__(self,b):
        return(Cell(self.count*b.count))
    
    def __truediv__(self,b):
        return(Cell(int(self.count/b.count)))
    
    def make_order(self,n):
        ost=self.count
        s=''
        while ost>0:
            if ost>=n:
                s+='*'*n
                s+='\n'
                ost-=n
            else:
                s+='*'*ost
                s+='\n'
                ost=0
            
        return s
    

a=Cell(5)
b=Cell(4)

c=a+b
d=a-b
e=a/b
f=a*b
s=f.make_order(3)
print(f.make_order(3))