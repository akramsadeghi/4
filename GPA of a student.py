# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 01:26:33 2022

@author: shabdar
"""


# GPA of a student

name = input("لطفا نامتان را وارد کنید")
family = input("لطفا نام خانوادگی را وارد کنید")
a = float(input("نمره درس اول را وارد کنید"))
b = float(input("نمره درس دوم را وارد کنید"))
c = float(input("نمره درس سوم را وارد کنید"))

gpa =float((a+b+c)/3)

if gpa>=17:
    print(name,family,"معدل شما در سطح عالی می باشد")
    
if gpa<17 and gpa>=12:
    print("معدل شما در سطح نرمال است")
    
if gpa<12:
    print("معدل شما در سطح مردود است")
    
print(gpa)    
    
