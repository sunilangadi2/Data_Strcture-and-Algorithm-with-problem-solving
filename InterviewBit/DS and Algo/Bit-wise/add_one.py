# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:25:02 2018

@author: Sunil Angadi
"""
"""To add 1 to a number x (say 0011000111),
 flip all the bits after the rightmost 0 bit (we get 0011000000). 
 Finally, flip the rightmost 0 bit also (we get 0011001000) to get the answer
"""
""" This also helps to get hang of spyder by giving negative number"""
# Python3 code to add 1
# one to a given number 
def addOne(x) :
     
    m = 1;
    # Flip all the set bits
    # until we find a 0 
    while(x & m):
        x = x ^ m
        m <<= 1
     
    # flip the rightmost 
    # 0 bit 
    x = x ^ m
    return x
 
# Driver program
n = 0
print (addOne(n))
