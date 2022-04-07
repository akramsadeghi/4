# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:57:26 2022

@author: shabdar
"""


 # Triangle
 # شرط لازم برای رسم مثلث: اندازه هر ضلع از مجموع دو ضلع دیگر کوچکتر باشد
ab = float(input("اندازه ضلع اول مثلث را وارد کنید"))
ac = float(input("اندازه ضلع دوم مثلث را وارد کنید"))
bc = float(input("اندازه ضلع سوم مثلث را وارد کنید"))


if ab< ac+bc:
    if ac < ab+bc:
        if bc < ab+ac:
            print("این مثلث قابل رسم است")
        else:
            print("اندازه ضلع سوم تصحیح شود")
    else:
        print("اندازه ضلع دوم تصحیح شود")  
else:
    print("اندازه ضلع اول تصحیح شود")     

    
    