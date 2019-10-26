# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:05:13 2018

@author: Sunil Angadi
"""

""" print second largest element in alist """

""" Convert list to set so that all duplicates will be removed
    then sort it use index -2 """
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(set(arr))
    arr.sort()
    print(arr[-2])