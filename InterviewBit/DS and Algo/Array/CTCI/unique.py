# -*- coding: utf-8 -*-
"""
Created on Wed May  2 14:22:56 2018

@author: Sunil Angadi
"""

# Python program to check if two 
# to get unique values from list
# using traversal 
 
# function to get unique values
def unique(list1):
 
    # just use set()
    return set(list1)
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        print (x),
     
   
 
# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
print(unique(list1))
 
 
list2 =[1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
print(unique(list2))
