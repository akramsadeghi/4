# -*- coding: utf-8 -*-
"""
Created on Thu May  5 01:11:34 2022

@author: shabdar
"""

def moadeleh_darajehdo(a,b,c):
    # (a*x^2)+(b*x)+c=0
    q=float(((b**2)-(4*a*c)))
    
    if q>0 :
        print( " معادله دو ریشه حقیقی دارد ")
        x1 = ((-b + q**0.5)/(2*a))
        x2 = ((-b - q**0.5)/(2*a))
        print(x1,x2) 
    elif q<0 :
        print("معادله دو ریشه مختلط دارد") 
        q=(-1)* q
        
        print("x1=",-b,"+","i",q**0.5,"/",2*a)
        print("x2=",-b,"-","i",q**0.5,"/",2*a)
    elif q==0 :
        print("معادله یک ریشه مضاعف دارد")
        x=((-b/2*a))
        print(x)
        
  
print("معادله درجه 2 با این شکل است. (ax2)+(bx)+c=0 ") 
a=float(input("a = "))   
b=float(input("b = ")) 
c=float(input("c = ")) 
moadeleh_darajehdo(a,b,c)

