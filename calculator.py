# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# calculator

a = float(input("عدد اول را وارد کنید"))
b = float(input("عدد دوم را وارد کنید"))
op = input("علامت عملگر را وارد کنید")

import math

if op == "+":
    result = a + b
    
if op == "*":
    result = a * b 
    
if op == "-":
    result = a - b
    
if op == "/":
    if b != 0:
        result = a / b  
    else :
        result ="این تقسیم ممکن نیست"

if op == "sin":
    # توابع مثلثاتی بر اساس رادیان محاسبه می شوند .
    result1 = math.sin(a/360.0*2*math.pi)
    result2 = math.sin(b/360.0*2*math.pi)
    print ("سینوس عدد اول",result1 ,"سینوس عدد دوم", result2)
    result ="هر دو عدد محاسبه شد." 
    
if op == "cos":
    # توابع مثلثاتی بر اساس رادیان محاسبه می شوند .
    result1 = math.cos(a/360.0*2*math.pi)
    result2 = math.cos(b/360.0*2*math.pi)
    print ("کسینوس عدد اول",result1 ,"کسینوس عدد دوم", result2)
    result ="هر دو عدد محاسبه شد."  
    
if op == "cot":
    result1 = math.cos(a/360.0*2*math.pi)/math.sin(a/360.0*2*math.pi)
    result2 = math.cos(b/360.0*2*math.pi)/math.sin(b/360.0*2*math.pi)
    print ("کتانژانت عدد اول",result1 ,"کتانژانت عدد دوم", result2)
    result ="هر دو عدد محاسبه شد."   
    

if op == "fac":
    factorial = 1
    for i in range(1 , int(a+1)): 
            factorial = factorial * i
    print ("رادیکال عدد اول",factorial)
    factorial = 1
    for i in range(1 , int(b+1)): 
            factorial = factorial * i
    print ("رادیکال عدد دوم",factorial)
    result ="هر دو عدد محاسبه شد."     
    
print(result)        

        