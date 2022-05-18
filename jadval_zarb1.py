# -*- coding: utf-8 -*-
"""
Created on Fri May  6 13:59:36 2022

@author: shabdar
"""


def jadval_zarb(n):
    print("x",end=" ")
    for i in range(1,n+1):
        if i<n+1:
            print(i,"--",end=" ")
        else:
            print(i,"--")
        #for j in range(1,n+1):
        
    for j in range(1,n+1):
        if j==1 :
            print('\n1',"--",end =" ")
            for z in range(1,n+1):
                
                print(j*z,"--",end =" ")
            print()
        else:
            for z in range(1,n+1):
                if z==1:
                    print(j,"--",j*1,"--",end =" ")
                else:    
                    print(j*z,"--",end =" ")
                   
            print()
        
     
n = int(input("طول جدول ضرب را وارد کنید: "))  
jadval_zarb(n)  
