import pygame
import os
import calendar

class Person:
    def __init__(self):
        self.x = 100
        self.y = 200
        
    def __str__(self):
        return str(self.x) +"   "+str(self.y)
    
p = Person()
print()




class Bus:
    def __init__(self):
        pass
        
    def doShow(self , fold_name):
        lists = os.listdir(fold_name)
        
        for name in lists:
            print(name)
        
        
bus = Bus()
bus.doShow("D://")

month_list = []
month = 1
 
while month <=12 :
	cal = calendar.month(2018,month)
	 month_list.append(cal)
	month+=1

for m in month_list:
	print(m)

#print(cal)
