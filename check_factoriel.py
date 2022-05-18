# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:25:06 2022

@author: shabdar
"""



def chek_factor(a):
    b=1
    z=1
    #b=1if a%b==0:
        
    while a%b==0 :
        print(b)
        b=b+1
    # else:
    #     print("این عدد فاکتوریل نیست")     
        
    for i in range(1,b):
        z=z*i
        if z==a:
            print("این عدد فاکتوریل ",i,"می باشد")
      
    
    
a= float(input("عدد مورد نظر را وارد کنید"))   
chek_factor(a) 
    
        
               
       