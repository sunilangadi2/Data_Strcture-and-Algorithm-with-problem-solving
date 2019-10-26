# -*- coding: utf-8 -*-
"""
Created on Wed May  2 19:26:32 2018

@author: Sunil Angadi
"""
""" this gives the element which appeared odd number of time in a list"""
from collections import Counter
#z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
z=[1,1,3,3,1,5,5,2,5,4]
c=Counter(z)
print(c)
for k,v in c.items():
	if v==1:  # number apper only once
		print(k)
