# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:57:27 2022

@author: shabdar
"""

#  B.M.M & K.M.M

def BMM_KMM(a,b):
    p = []
    q = []
    
    
    for i in range (1,a+1):
        d = a%i
        if d==0:
           p.append(i) 
           
    print("طول لیست مقسوم علیه های عدد اول=",len(p),"لیست مقسوم علیه های عدد اول=",p)       
    
    for i in range (1,b+1):
        d = b%i
        if d==0:
           q.append(i) 
           
    print("طول لیست مقسوم علیه های عدد دوم=",len(q),"لیست مقسوم علیه های عدد دوم=",q)       
    
    z=[]
    
    for i in range(0,len(p)):       
        if p[i] in q:
            z.append(p[i])
            i=i+1
          
      
    if len(z) ==1:
        print("B.M.M = K.M.M") 
    else:
        print("K.M.M=",z[0])
        w=len(z)
        print("B.M.M=",z[w-1])
    
    print("لیست مقسوم علیه های مشترک=",z)          


a = int(input("عدد اول را وارد کنید"))
b = int(input("عدد دوم را وارد کنید"))
BMM_KMM(a,b)

