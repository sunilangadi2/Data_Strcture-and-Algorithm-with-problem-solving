# -*- coding: utf-8 -*-
"""
Created on Fri May  4 11:12:16 2018

@author: Sunil Angadi
"""

mylist=[0,1,2,2,4,5,5,5,8]
item=5
# logic just start from reverse
for i in range(len(mylist)-1,-1,-1):
    if mylist[i] == item:
        index = i
        print(index)
        break