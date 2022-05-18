# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:33:07 2022

@author: shabdar
"""
def word_number(t):

    txt = t.strip() 
    x = txt.count(" ")
    print(x+1)

t=input("جمله دلخواه را وارد کنید")

word_number(t)