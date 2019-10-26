# -*- coding: utf-8 -*-

"""
Created on Sun Jun  3 19:16:51 2018

@author: Sunil Angadi
"""

""" Print second lowest grade student name"""

""" Use set and sort it at index 1 we will get second lowest then 
    match that marks to the name, marks in the marks sheet"""

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]
print((*[a for a,b in sorted(marksheet) if b == second_lowest])) # * for unpacking
