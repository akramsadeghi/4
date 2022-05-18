# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:37:28 2022

@author: shabdar
"""

#پر کردن یک لیست با اعداد تصادفی و غیر تکراری
import random
my_list=[]

n = int(input("طول لیست را اعلام کنید:"))
a=int(input("شروع: "))
b=int(input("پایان: "))
for i in range(n):
    q=random.randint(a, b)
    if q in my_list:
        q=random.randint(a, b)
    else:    
        my_list.append(q)
        my_list=list(set(my_list))
my_list.sort()
a=len(my_list)
print(my_list)
if n>a:
    print("به دلیل محدوده کوچکتر از طول لیست ،اندازه لیست کوچکتر از مقدار تعیین شده است ")
    print("آیا اعداد اعشاری هم در لیست قرار بگیرد؟ y or n")
    r=input()
    if r=="y":
        m_list=[]
        m=n-a
        for j in range(m):
            g=random.random() * (b - a) + a
            if g in my_list:
                g=random.randint(a, b)
            m_list.append(g)
            m_list=list(set(m_list))
        print(m_list)
        my_list=my_list+m_list
        my_list.sort()  
    else:
        print("تعداد اعضای لیست شما کمتر از مقدار خواسته شده است")
           
print(my_list)



    
