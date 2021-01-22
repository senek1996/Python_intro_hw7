# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 22:57:49 2021

@author: Lenovo
"""

def zeros(r,c):
    #лист листов размера r*c из нулей
    m=[[0]*c]*r
    return m

class Matrix:
    
    def __init__(self,lst):
        l_prev=len(lst[0])
        if len(lst)>1:
            for i in range(1,len(lst)):
                if len(lst[i])!=l_prev:
                    raise ValueError('Длины всех строк в матрице должны быть\
                                     равны!')
                
                l_prev=len(lst[i])
                
            
        self.c=len(lst[0])  #количество столбцов
        self.r=len(lst)     #количество строк
        self.data=lst       #данные матрицы
    
    def __str__(self):
        s=''
        for r in self.data:
            for c in r:
                s+='{0:5d} '.format(c)
            
            s+='\n'
        
        return(s)
    
    def __add__(self,b):
        if self.r!=b.r or self.c!=b.c:
            raise ValueError('Размеры складываемых матриц должны быть равны!')
        else:
            a_data=self.data
            b_data=b.data
            c_data=[]
            for i in range(self.r):
                row=[]
                for j in range(self.c):
                    row.append(a_data[i][j]+b_data[i][j])
                
                c_data.append(row)
                
            return Matrix(c_data)
    


a=Matrix([[2,4,1],[3,5,2]])
b=Matrix([[4,8,3],[5,9,12]])
c=a+b
print(str(a),end='\n\n')
print(str(b),end='\n\n')
print('Результат сложения: \n'+str(c))