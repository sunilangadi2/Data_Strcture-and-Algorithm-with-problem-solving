# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:51:51 2018

@author: Sunil Angadi
"""

""" Count number of times substring appears in the given string """

def count_substring(string, sub_string):
    c=0 
    for i in range(len(string)):
    	if sub_string in string[i:i+len(sub_string)]:
    		c+=1
    return c

if __name__=='__main__':
    string='sunilsuni'
    sub_string='su'
    print(count_substring(string,sub_string))