# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:03:05 2022

@author: shabdar
"""

w = ['shirmoz', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'book']

import random

answer = random.choice(w)

print('- ' * len(answer))
print(" بازی را چگونه انجام میدهید :برای حدس حروف عدد 1 و برای حدس کلمه عدد 2 را وارد کنید")
r=int(input())
if r==1:
    cont=0
    for word in answer:
        cont +=1
    x=(cont*"-")    
    n=list(x)   
    y= input("یک حرف وارد کن: ")
    joon = 0
    while "-" in n:
        x2=""
        if y.lower() in answer:
            for z in range(0,len(answer)):
                if answer[z]==y.lower():
                   n[z]=answer[z]
                x2 = x2 + n[z]
            print(x2)
            if "-" in n:
              y= input("آفرین یه حرف دیگه وارد کن: ")
    
        else:
              joon-=1
              print("شما حدس اشتباه داشتید: ", joon)
              y= input("حرفی که گفتی اشتباه بود یکی دیگه وارد کن: ")
    if joon==0:
        print("شما تمام حروف را درست حدس زدید و برنده شدید.")   
    else:
        print("شما امتیاز منفی دارید: ",joon) 
        #break;          
              
if r==2:
    joon = 10

    while joon > 0:
        
        user_character1 = input() # s
        user_character=user_character1.lower()
        

        if user_character in answer:
            
            print('yes')
            break
        else:
            joon = joon - 1
            print('no')    
            
            
    if joon==10:
        print("*شما با اولین حدس برنده شدید*")
                
    print (joon)              
    
    
