# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:49:51 2018

@author: Sunil Angadi
"""

# Python3 program to check if given
# number is power of 4 or not 

# Logic: By checkng until it reaches to 1
# This also works for all x is power of n
 
# Function to check if x is power of 4
def isPowerOfFour(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 4 != 0):
            return False
        n = n // 4         
    return True
 
# Driver code
test_no = 32
if(isPowerOfFour(test_no)):
    print(test_no, 'is a power of 4')
else:
    print(test_no, 'is not a power of 4')