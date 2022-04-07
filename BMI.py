# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:50:37 2022

@author: shabdar
"""


# BMI
#عدد حجم توده بدن=وزن بر حسب کیلوگرم/قد بر حسب متر به توان 2
weight = float(input("وزنتان را بر حسب کیلوگرم وارد نمائید"))
height = float(input("قدتان را برحسب متر وارد کنید"))
bmi = weight/height**2
if bmi<18.5:
    print(" شما دچار کم وزنی هستید")
    
if 18.5<bmi<24.9:
    print("شما در بازه وزن سالم هستید")   
    
if 25<bmi<29.9:
    print("شما دچار اضافه وزن هستید")
    
if 30<bmi<39.9:
    print("شما دچار چاقی مفرط هستید")  
print(bmi)

