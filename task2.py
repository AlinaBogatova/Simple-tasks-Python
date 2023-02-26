# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:40:31 2022

@author: User
"""

name = 'BMW X1'
driver_age = round(float(input('Возраст: ')))
experience = 10
reputation = 5
traffic = 4
duration = 25
price = 0
rate = 0

if name == 'volkswagen polo':
    if 20<=driver_age<=27:
        if 2<=experience<=9:
            if 1<=reputation<=2:
                if 1<=traffic<=3:
                    rate = 8
                elif 4<=traffic<=7:
                    rate = 8.5
            elif 3<=reputation<=5:
                if 1<=traffic<=3:
                    rate = 7.5
                elif 4<=traffic<=7:
                    rate = 7.4
                
    if 27<=driver_age<=34:
        if 2<=experience<=9:
            if 1<=reputation<=2:
                rate =7.2
            elif 3<=reputation<=5:
                if 1<=traffic<=3:
                    rate = 7
                elif 4<=traffic<=7:
                    rate = 7.2
        elif 10<=experience<=15:
            if 1<=reputation<=2:
                if 1<=traffic<=3:
                    rate = 6.9
                elif 4<=traffic<=7:
                    rate = 6.7
            elif 3<=reputation<=5:
                rate = 6.6
elif name == 'BMW X1':
    if 20<=driver_age<=27:
        if 2<=experience<=9:
            if 1<=reputation<=2:
                if 1<=traffic<=3:
                    rate = 12
                elif 4<=traffic<=7:
                    rate = 12.5
            elif 3<=reputation<=5:
                if 1<=traffic<=3:
                    rate = 11.6
                elif 4<=traffic<=7:
                    rate = 11.3
                
    if 27<=driver_age<=34:
        if 2<=experience<=9:
            if 1<=reputation<=2:
                rate =11.4
            elif 3<=reputation<=5:
                if 1<=traffic<=3:
                    rate = 11.7
                elif 4<=traffic<=7:
                    rate = 11.9
        elif 10<=experience<=15:
            if 1<=reputation<=2:
                if 1<=traffic<=3:
                    rate = 10.8
                elif 4<=traffic<=7:
                    rate = 11
            elif 3<=reputation<=5:
                rate = 10.9
print('Стоимость поездки составит ', duration*rate)