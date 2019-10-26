# -*- coding: utf-8 -*-
"""
Created on Wed May  2 14:36:30 2018

@author: Sunil Angadi
"""

# Python3 code to find the element 
# that occur only once
def getSingle(arr,n):
    visited=[False for i in range(n)]
    for i in range(0,n):
        x=arr[i]
        if(visited[i]==False):
            isduplicate=False
            for j in range(i+1,n):
                if(x==arr[j]):
                    isduplicate=True
                    visited[j]=True
            if(isduplicate==False):
               print("The element with single occurrence is %s " %(x))
                    
            
                
# Driver program
#arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3,4]
arr=[5,5,2,2,4,3,5]
n = len(arr)
getSingle(arr, n)
c=arr.count(5)
print(c)
 