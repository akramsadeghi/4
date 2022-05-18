# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 01:58:04 2022

@author: shabdar

"""

#رسم شکل چهارگوش با* و # به صورت یک در میان 
def Row(n):
    for j in range(n):
        if j%2==0 :
            print("*",end=' ')
        else:
            print("#",end=' ')
    
def Rov(n):
    for j in range(n):
        if j%2==0 :
            print("#",end=' ')
        else:
            print("*",end=' ')
            
            
            
n=int(input("طول شکل  را برای رسم مشخص کنید:"))
m=int(input("ارتفاع شکل  را برای رسم مشخص کنید:"))
for i in range(m):
    if i%2==0 :
        Row(n)
    else:  
        Rov(n)
        
    print()    